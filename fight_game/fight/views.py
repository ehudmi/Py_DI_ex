from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
import requests
import json
from random import randint

from .forms import CustomUserCreationForm
from .models import FightUser, Figure

with open("config/_env_var.json") as file:
    data = json.load(file)
API_KEY = data["MY_API_KEY"]


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def get_figure(request):
    url = "https://historical-figures-by-api-ninjas.p.rapidapi.com/v1/historicalfigures"

    querystring = {"name": "painter"}

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


def get_image(request):
    url = "https://bing-image-search1.p.rapidapi.com/images/search"

    querystring = {"q": "william shakespeare"}

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
                "name": image["name"],
                "thumbnail": image["thumbnailUrl"],
                "image_url": image["contentUrl"],
            }
        )
    return render(request, "fight/images.html", context)
