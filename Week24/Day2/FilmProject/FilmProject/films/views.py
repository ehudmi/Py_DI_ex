from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Film, Director
from .forms import FilmForm, DirectorForm, ReviewForm
from django.views.generic import ListView, CreateView, UpdateView


class HomePageView(ListView):
    model = Film
    template_name = "films/homepage.html"
    context_object_name = "films"


class FilmCreateView(CreateView):
    form_class = FilmForm
    template_name = "film/addFilm.html"
    success_url = reverse_lazy("homepage")


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
