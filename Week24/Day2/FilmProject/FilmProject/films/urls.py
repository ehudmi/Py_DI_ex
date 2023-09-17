from django.urls import path
from . import views

urlpatterns = [
    path(
        "films/homepage",
        views.HomePageView.as_view(template_name="films/homepage.html"),
        name="homepage",
    ),
    path(
        "films/addFilm",
        views.FilmCreateView.as_view(template_name="film/addFilm.html"),
        name="add-film",
    ),
    path(
        "director/addDirector",
        views.DirectorCreateView.as_view(template_name="director/addDirector.html"),
        name="add-director",
    ),
]
