from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView
from django.contrib import messages
from random import randint
from faker import Faker
from .forms import CustomUserCreationForm, SearchFigure
from .models import FightUser, Figure, FigureImage, Battle
from .services import get_API_figure, get_API_image, calc_score

fake = Faker()


# sign up view
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class HomeView(TemplateView):
    template_name = "fight/home.html"


# search for a figure
def search_figure(request):
    context = {}
    if request.method == "POST":
        form = SearchFigure(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            occupation = form.cleaned_data["occupation"]
            context["form"] = {"name": name, "occupation": occupation}
            # if the user has input a name but no occupation, search for figures with that name
            if occupation == "":
                context["figures"] = Figure.objects.filter(name__icontains=name).all()
                if context["figures"].count() == 0:
                    messages.info(
                        request,
                        f"No figures with name {name} found in db. Retrieving from API.",
                    )
                    context["figures"] = get_API_figure(request, name, randint(0, 10))
            # if the user has input an occupation but no name, search for figures with that occupation
            elif name == "":
                context["figures"] = Figure.objects.filter(
                    occupation__icontains=occupation
                ).all()
                if context["figures"].count() == 0:
                    messages.info(
                        request,
                        f"No figures with occupation {occupation} found in db. To Search the API - input just name.",
                    )
                    context["figures"] = get_API_figure(
                        request, f"{name} ({occupation})", randint(0, 10)
                    )
            # if the user has input both a name and an occupation, search for figures with both
            else:
                context["figures"] = Figure.objects.filter(
                    occupation__icontains=occupation, name__icontains=name
                ).all()
                if context["figures"].count() == 0:
                    messages.info(
                        request,
                        f"No figures with name {name} and occupation {occupation} found in db. To Search the API - input just name.",
                    )
                    context["figures"] = get_API_figure(
                        request, f"{name} ({occupation})", randint(0, 10)
                    )
            return render(request, "figure/search_results.html", context)
    else:
        form = SearchFigure()
        context["form"] = form
    return render(request, "figure/search_figure.html", context)


# after selecting a figure, get images for that figure
def after_select_figure(request):
    if request.method == "POST":
        figure = Figure.objects.filter(name=request.POST.get("name")).first()
        if figure is None:
            figure = Figure.objects.create(
                name=request.POST.get("name"),
                title=request.POST.get("title"),
                occupation=request.POST.get("occupation"),
            )
        return redirect("get-images", figure.pk)
    else:
        return redirect("search-figure")


# get images for a figure
def get_images(request, id):
    context = {}
    figure = Figure.objects.filter(pk=id).first()
    if figure is not None:
        context["figure"] = figure
        images = FigureImage.objects.filter(figure=figure).all()
        if images.count() > 0:
            context["images"] = images
        if list(images) == []:
            context["images"] = get_API_image(request, figure.name)
    return render(request, "figure/image_select.html", context)


# after selecting an image, add it to the figure
def after_select_image(request, id):
    context = {}
    figure = Figure.objects.filter(pk=id).first()
    if figure is not None:
        image = FigureImage.objects.filter(pk=request.POST.get("id")).first()
        if image is None:
            image = FigureImage.objects.create(
                pk=request.POST.get("id"),
                name=request.POST.get("name"),
                image_url=request.POST.get("image_url"),
                figure=figure,
            )
            battle_hero = Battle.objects.filter(figure=figure).first()
            if request.user.is_authenticated and battle_hero is None:
                add_to_battle = Battle.objects.create(
                    figure=figure, image=image, player=request.user
                )
                scores = calc_score(figure.notoriety, figure.luck)
                update_battle = Battle.objects.filter(figure=figure).update(
                    notoriety=scores["notoriety"],
                    intelligence=scores["intelligence"],
                    strength=scores["strength"],
                    luck=scores["luck"],
                    score=scores["score"],
                )
                context["scores"] = scores
        context["figure"] = figure
        context["image"] = image

    return render(request, "fight/my_hero.html", context)


# create an opponent by name
def create_opponent_by_name(request):
    rival = {}
    rival_name = fake.first_name()
    print(rival_name)
    rivals = Figure.objects.filter(name__icontains=rival_name).all()
    # if there are no figures with that name in the db, get a random figure from the API
    if rivals.count() == 0:
        while get_API_figure(request, rival_name, randint(0, 10)) == []:
            rival_name = fake.first_name()
            get_rival = get_API_figure(request, rival_name, 0)[randint(0, 10)]
        else:
            get_rival = get_API_figure(request, rival_name, 0)[randint(0, 10)]
            print(get_rival)
            rival = Figure.objects.create(
                name=get_rival["name"],
                title=get_rival["title"],
                occupation=get_rival["occupation"],
            )
            # get images for the figure
            rival_images = get_API_image(request, get_rival["name"])
            get_image = rival_images[randint(0, len(rival_images) - 1)]
            image = FigureImage.objects.create(
                id=get_image["id"],
                name=get_image["name"],
                image_url=get_image["image_url"],
                figure=rival,
            )
    # add the figure to the battle
    else:
        rival = rivals[randint(0, rivals.count() - 1)]
        images = FigureImage.objects.filter(figure=rival).all()
        image = images[randint(0, images.count() - 1)]
    battle_rival = Battle.objects.filter(figure=rival).first()
    if request.user.is_authenticated and battle_rival is None:
        add_to_battle = Battle.objects.create(figure=rival, image=image)
    # update the battle with the figure's attributes
    scores = calc_score(rival.notoriety, rival.luck)
    update_battle = Battle.objects.filter(figure=rival).update(
        notoriety=scores["notoriety"],
        intelligence=scores["intelligence"],
        strength=scores["strength"],
        luck=scores["luck"],
        score=scores["score"],
    )

    return redirect("battle")


# create an opponent by occupation
def create_opponent_by_occupation(request):
    rival = {}
    rival_name = fake.first_name()
    print(rival_name)
    occupation = request.POST.get("occupation")
    if occupation != "":
        rivals = Figure.objects.filter(occupation__icontains=occupation).all()
        # if there are no figures with that occupation in the db, get a random figure from the API
        if rivals.count() == 0:
            while get_API_figure(request, rival_name, randint(0, 10)) == []:
                rival_name = fake.first_name()
                get_rival = get_API_figure(request, f"{rival_name} ({occupation})", 0)[
                    randint(0, 10)
                ]
            else:
                get_rival = get_API_figure(request, f"{rival_name} ({occupation})", 0)[
                    randint(0, 10)
                ]
                rival = Figure.objects.create(
                    name=get_rival["name"],
                    title=get_rival["title"],
                    occupation=get_rival["occupation"],
                )
                # get images for the figure
                rival_images = get_API_image(request, get_rival["name"])
                get_image = rival_images[randint(0, len(rival_images) - 1)]
                image = FigureImage.objects.create(
                    id=get_image["id"],
                    name=get_image["name"],
                    image_url=get_image["image_url"],
                    figure=rival,
                )
        else:
            rival = rivals[randint(0, rivals.count() - 1)]
            images = FigureImage.objects.filter(figure=rival).all()
            image = images[randint(0, images.count() - 1)]
        battle_rival = Battle.objects.filter(figure=rival).first()
        if request.user.is_authenticated and battle_rival is None:
            add_to_battle = Battle.objects.create(figure=rival, image=image)
            # update the battle with the figure's attributes
        scores = calc_score(rival.notoriety, rival.luck)
        update_battle = Battle.objects.filter(figure=rival).update(
            notoriety=scores["notoriety"],
            intelligence=scores["intelligence"],
            strength=scores["strength"],
            luck=scores["luck"],
            score=scores["score"],
        )
    return redirect("battle")


class BattleView(ListView):
    model = Battle
    template_name = "fight/battle.html"
    context_object_name = "battle"
