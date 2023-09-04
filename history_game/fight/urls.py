from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("get_figure/", views.get_figure, name="get-figure"),
    path("get_image/", views.get_image, name="get-image"),
]
