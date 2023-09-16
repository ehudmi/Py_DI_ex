from django.urls import path
from . import views

urlpatterns = [
    path("", views.display_gifs, name="display-gifs"),
    path("add_category", views.add_category, name="add-category"),
    path("list_categories", views.show_categories, name="list-category"),
    path("<gif_id>/<int:counter>", views.like_add, name="like-add"),
    path("like_gifs", views.sort_like, name="like-gifs"),
]
