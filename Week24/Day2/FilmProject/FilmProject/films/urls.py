from django.urls import path
from . import views

urlpatterns = [
    path(
        "films/homepage",
        views.HomePageView.as_view(),
        name="homepage",
    ),
    path(
        "films/addFilm",
        views.film_add,
        name="add-film",
    ),
    path(
        "director/addDirector",
        views.DirectorCreateView.as_view(),
        name="add-director",
    ),
    path(
        "films/editFilm/<pk>",
        views.FilmUpdateView.as_view(),
        name="edit-film",
    ),
    path(
        "director/editDirector/<pk>",
        views.DirectorUpdateView.as_view(),
        name="edit-director",
    ),
    path(
        "review/addReview/",
        views.ReviewCreateView.as_view(),
        name="add-review",
    ),
    path("poster/addPoster/", views.PosterCreateView.as_view(), name="add-poster"),
    path(
        "films/deleteFilm/<pk>",
        views.FilmDeleteView.as_view(),
        name="delete-film",
    ),
]
