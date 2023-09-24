from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Film, Director, Poster
from .forms import FilmForm, DirectorForm, ReviewForm, PosterForm
from django.views.generic import ListView, CreateView, UpdateView
from django.forms import modelformset_factory


class HomePageView(ListView):
    model = Film
    template_name = "films/homepage.html"
    context_object_name = "films"


def film_add(request):
    poster_formset = modelformset_factory(
        Poster, form=PosterForm, exclude=(["film"]), extra=1
    )
    if request.method == "POST":
        form = FilmForm(request.POST)
        formset = poster_formset(
            request.POST, request.FILES, queryset=Poster.objects.none()
        )
        if form.is_valid():
            film = form.save()
            if formset.is_valid():
                for form in formset.cleaned_data:
                    image = form["image"]
                    photo = Poster(film=film, image=image)
                    photo.save()
            return redirect("homepage")
    else:
        form = FilmForm()
        formset = poster_formset(queryset=Poster.objects.none())
    return render(request, "film/addFilm.html", {"form": form, "formset": formset})


class DirectorCreateView(CreateView):
    form_class = DirectorForm
    template_name = "director/addDirector.html"
    success_url = reverse_lazy("homepage")


class FilmUpdateView(UpdateView):
    model = Film
    form_class = FilmForm
    template_name = "film/editFilm.html"
    success_url = reverse_lazy("homepage")


class DirectorUpdateView(UpdateView):
    model = Director
    form_class = DirectorForm
    template_name = "director/editDirector.html"
    success_url = reverse_lazy("homepage")


class ReviewCreateView(CreateView):
    form_class = ReviewForm
    template_name = "review/addReview.html"
    success_url = reverse_lazy("homepage")


class PosterCreateView(CreateView):
    form_class = PosterForm
    template_name = "poster/addPoster.html"
    success_url = reverse_lazy("homepage")
