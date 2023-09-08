from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
import requests
import json
from random import randint

from .forms import CustomUserCreationForm, SearchFigure
from .models import FightUser, Figure

with open("config/_env_var.json") as file:
    data = json.load(file)
API_KEY = data["MY_API_KEY"]


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def get_figure(request, value, offset):
    url = "https://historical-figures-by-api-ninjas.p.rapidapi.com/v1/historicalfigures"

    querystring = {"name": value, "offset": offset}

    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "historical-figures-by-api-ninjas.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)
    figure_json = response.json()
    context = {"figures": []}
    for figure in figure_json:
        # print(figure)

        context["figures"].append(
            {
                "name": figure["name"],
                "title": figure["title"],
                "occupation": figure["info"].get("occupation", ""),
            }
        )

    return render(request, "fight/figures.html", context)


def get_image(request, name, id):
    url = "https://bing-image-search1.p.rapidapi.com/images/search"

    querystring = {"q": name}

    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "bing-image-search1.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)

    image_json = response.json()
    context = {"images": []}
    for image in image_json["value"]:
        context["images"].append(
            {
                "id": id,
                "name": image["name"],
                "thumbnail": image["thumbnailUrl"],
                "image_url": image["contentUrl"],
            }
        )
    return render(request, "fight/images.html", context)


def search_figure(request):
    context = {}
    context["page_title"] = "Search for Figure"
    if request.method == "POST":
        form = SearchFigure(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            occupation = form.cleaned_data["occupation"]
            context["form"] = {"name": name, "occupation": occupation}
            if occupation == "":
                return get_figure(request, name, 0)
            else:
                return get_figure(request, f"{name} ({occupation})", randint(0, 10))

        return render(request, "fight/search_figure.html", context)
    else:
        form = SearchFigure()
        context["form"] = form
    return render(request, "fight/search_figure.html", context)


def select_figure(request):
    context = {}
    context["page_title"] = "Select the Figure"
    if request.method == "POST":
        if (
            request.POST.get("name")
            != Figure.objects.filter(name=request.POST.get("name")).first().name
        ):
            figure = Figure.objects.create(
                name=request.POST.get("name"),
                title=request.POST.get("title"),
                occupation=request.GET.get("occupation"),
            )
            return get_image(request, request.POST.get("name"), figure.pk)
        else:
            figure = Figure.objects.filter(name=request.POST.get("name")).first()
            context["figure"] = figure
            return render(request, "fight/battle_screen.html", context)


def select_image(request):
    context = {}
    if request.method == "POST":
        figure = Figure.objects.filter(id=request.POST.get("id"))
        figure.update(image_url=request.POST.get("image_url"))
        context["figure"] = figure
        # create_opponent()

    return render(request, "fight/battle_screen.html", context)


def user_figure(request):
    context = {}
    context["page_title"] = "Your selected Figure"


def create_opponent():
    pass
