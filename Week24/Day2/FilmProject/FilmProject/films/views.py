from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Film
from .forms import FilmForm, DirectorForm
from django.views.generic import ListView, CreateView


class HomePageView(ListView):
    model = Film
    context_object_name = "films"


class FilmCreateView(CreateView):
    form_class = FilmForm
    success_url = reverse_lazy("homepage")


class DirectorCreateView(CreateView):
    form_class = DirectorForm
    success_url = reverse_lazy("homepage")
