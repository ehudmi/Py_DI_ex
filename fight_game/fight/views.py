from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, DetailView
from django.contrib import messages
from random import randint
from faker import Faker
from .forms import CustomUserCreationForm, SearchFigure
from .models import FightUser, Figure, FigureImage, Battle
from .services import (
    get_API_figure,
    get_API_image,
    get_API_WIKI_info,
    calc_score,
    replace,
)

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
                context["name"] = name
                figures = Figure.objects.filter(name__icontains=name).all()
                if figures.count() < 10:
                    context["figures"] = (
                        list(figures)
                        + get_API_figure(request, name, randint(0, 10))[
                            0 : 10 - figures.count()
                        ]
                    )
                    if figures.count() == 0:
                        messages.info(
                            request,
                            f"No figures with name {name} found in db. Retrieving from API.",
                        )
                    else:
                        messages.info(
                            request,
                            f"Some figures with name {name} found in db. Retrieved more from API.",
                        )
            # if the user has input an occupation but no name, search for figures with that occupation
            elif name == "":
                context["occupation"] = occupation
                figures = Figure.objects.filter(occupation__icontains=occupation).all()
                if figures.count() < 10:
                    context["figures"] = (
                        list(figures)
                        + get_API_figure(
                            request, f"{name} ({occupation})", randint(0, 10)
                        )[0 : 10 - figures.count()]
                    )
                    if figures.count() == 0:
                        messages.info(
                            request,
                            f"No figures with occupation {occupation} found in db. Retrieving from API.",
                        )
                    else:
                        messages.info(
                            request,
                            f"Some figures with occupation {occupation} found in db. Got more from API.",
                        )
            # if the user has input both a name and an occupation, search for figures with both
            else:
                context["name"] = name
                context["occupation"] = occupation
                figures = Figure.objects.filter(
                    occupation__icontains=occupation, name__icontains=name
                ).all()
                if figures.count() < 10:
                    context["figures"] = (
                        list(figures)
                        + get_API_figure(
                            request, f"{name} ({occupation})", randint(0, 10)
                        )[0 : 10 - figures.count()]
                    )
                    if figures.count() == 0:
                        messages.info(
                            request,
                            f"No figures with name {name} and occupation {occupation} found in db. Retrieving from API.",
                        )
                    else:
                        messages.info(
                            request,
                            f"Some figures with name {name} and occupation {occupation} found in db. Retrieved more from API",
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
        if images.count() < 10:
            context["images"] = (
                list(images)
                + get_API_image(request, figure.name)[0 : 10 - images.count()]
            )
            if images.count() == 0:
                messages.info(
                    request,
                    f"No images found in db for {figure.name}. Retrieving from API.",
                )
            else:
                messages.info(
                    request,
                    f"Some images found in db for {figure.name}. Retrieved more from API.",
                )
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
    while get_API_figure(request, rival_name, randint(0, 10)) == []:
        rival_name = fake.first_name()
        get_rival = get_API_figure(request, rival_name, randint(0, 10))[randint(0, 10)]
        print("here", get_rival, rival_name)
    else:
        get_rival = get_API_figure(request, rival_name, randint(0, 10))[randint(0, 10)]
        print("here1", get_rival, rival_name)
        new = (
            Figure.objects.filter(name=get_rival["name"])
            .filter(title=get_rival["title"])
            .all()
        )
        print(new)
    if (
        Figure.objects.filter(name=get_rival["name"])
        .filter(title=get_rival["title"])
        .count()
        == 0
    ):
        rival = Figure.objects.create(
            name=get_rival["name"],
            title=get_rival["title"],
            occupation=get_rival["occupation"],
        )
        print("here2", rival, rival_name)
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
        rival = (
            Figure.objects.filter(name=get_rival["name"])
            .filter(title=get_rival["title"])
            .first()
        )
        print("here3", rival, rival_name)
        images = FigureImage.objects.filter(figure=rival).all()
        image = images[randint(0, images.count() - 1)]
    # add the figure to the battle
    battle_rival = Battle.objects.filter(figure=rival).first()
    if request.user.is_authenticated and battle_rival is None:
        add_to_battle = Battle.objects.create(figure=rival, image=image)
    # update the battle with the figure's attributes
    if rival is not None:
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
def create_opponent_by_occupation(request, id):
    rival = {}
    figure = Figure.objects.filter(pk=id).first()
    if figure is not None:
        get_occupation = figure.occupation
        if get_occupation != "":
            fix_occupation = replace(
                get_occupation, {"[": "", "]": "", ", ": ",", "'": ""}
            )
            occupation_list = fix_occupation.split(",")
            occupation = occupation_list[randint(0, len(occupation_list) - 1)]
            while get_API_figure(request, f"({occupation})", randint(0, 10)) == []:
                rivals = get_API_figure(request, f"({occupation})", randint(0, 10))
                get_rival = rivals[randint(0, len(rivals) - 1)]
            else:
                rivals = get_API_figure(request, f"({occupation})", randint(0, 10))
                get_rival = rivals[randint(0, len(rivals) - 1)]
                print("here2", get_rival, occupation_list)
            if (
                Figure.objects.filter(name=get_rival["name"])
                .filter(title=get_rival["title"])
                .count()
                == 0
            ):
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
                rival = (
                    Figure.objects.filter(name=get_rival["name"])
                    .filter(title=get_rival["title"])
                    .first()
                )

                images = FigureImage.objects.filter(figure=rival).all()
                image = images[randint(0, images.count() - 1)]
            battle_rival = Battle.objects.filter(figure=rival).first()
            if request.user.is_authenticated and battle_rival is None:
                add_to_battle = Battle.objects.create(figure=rival, image=image)
                # update the battle with the figure's attributes
            if rival is not None:
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


class OutcomeView(ListView):
    model = Battle
    template_name = "fight/outcome.html"
    context_object_name = "battle"

    def get_queryset(self):
        battle = Battle.objects.all().order_by("-score")
        winner = battle.first()
        return winner


def cleanup(request):
    records = Battle.objects.all()
    records.delete()
    return redirect("home")


class ProfileView(ListView):
    model = FightUser
    template_name = "user/profile.html"
    context_object_name = "profile"

    def get_queryset(self):
        profile = FightUser.objects.filter(username=self.request.user).first()
        return profile


class ProfileFigureView(DetailView):
    model = Figure
    template_name = "user/profile_figure.html"
    context_object_name = "figure"

    def get_queryset(self):
        if self.kwargs.get("pk") is not None:
            figure = Figure.objects.filter(pk=self.kwargs.get("pk")).all()
            return figure

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        figure = Figure.objects.filter(pk=self.kwargs.get("pk")).first()
        images = FigureImage.objects.filter(figure=figure).all()
        image = images[randint(0, images.count() - 1)]
        context["image"] = image
        if figure is not None:
            context["wiki"] = get_API_WIKI_info(self.request, figure.name)
        return context
