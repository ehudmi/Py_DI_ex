from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    View,
    DetailView,
)
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from .models import Film, Director, Poster
from accounts.models import UserProfile
from .forms import FilmForm, DirectorForm, ReviewForm, PosterForm


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
            messages.success(
                request, f"{form.cleaned_data['title']} Added successfully"
            )
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


class DirectorCreateView(SuccessMessageMixin, CreateView):
    form_class = DirectorForm
    template_name = "director/addDirector.html"
    success_url = reverse_lazy("homepage")
    success_message = "%(first_name)s %(last_name)s Added successfully"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = User.objects.get(id=request.user.pk)
            if user.is_superuser:
                return super().dispatch(request, *args, **kwargs)
            else:
                return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)


class FilmUpdateView(UpdateView):
    model = Film
    form_class = FilmForm
    template_name = "film/editFilm.html"
    success_url = reverse_lazy("homepage")
    success_message = "%(title)s Updated successfully"


class DirectorUpdateView(SuccessMessageMixin, UpdateView):
    model = Director
    form_class = DirectorForm
    template_name = "director/editDirector.html"
    success_url = reverse_lazy("homepage")
    success_message = "%(first_name)s %(last_name)s Updated successfully"


class ReviewCreateView(CreateView):
    form_class = ReviewForm
    template_name = "review/addReview.html"
    success_url = reverse_lazy("homepage")
    success_message = "Review created successfully"

    def form_valid(self, form):
        form.instance.review_author = self.request.user
        return super().form_valid(form)


class PosterCreateView(CreateView):
    form_class = PosterForm
    template_name = "poster/addPoster.html"
    success_url = reverse_lazy("homepage")


class FilmDeleteView(SuccessMessageMixin, DeleteView):
    model = Film
    template_name = "film/confirm_delete.html"
    success_message = "%(title)s deleted successfully"
    success_url = reverse_lazy("homepage")

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user = User.objects.get(id=self.request.user.pk)
            if user.is_superuser:
                return super(FilmDeleteView, self).get_queryset()


class FavoriteFilmView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            film = Film.objects.get(pk=self.kwargs["pk"])
            user = User.objects.get(id=request.user.pk)
            if UserProfile.objects.filter(user=user):
                user_profile = UserProfile.objects.get(user=user)
            else:
                user_profile = UserProfile.objects.create(user=user)
            if user_profile.favorite_films.filter(pk=film.pk).exists():
                user_profile.favorite_films.remove(film)
                messages.success(request, f"{film.title} removed from favorites")
            else:
                user_profile.favorite_films.add(film)
                messages.success(request, f"{film.title} added to favorites")
            return redirect("homepage")
        else:
            return HttpResponseForbidden()


class FilmDetailView(DetailView):
    model = Film
    template_name = "film/filmDetail.html"
    context_object_name = "film"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        film = context["object"]
        reviews = film.review_set.all()
        context["reviews"] = reviews
        return context
