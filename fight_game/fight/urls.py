from django.urls import path

from . import views

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("get_figure/", views.get_figure, name="get-figure"),
    path("get_image/", views.get_image, name="get-image"),
    path("search_figure/", views.search_figure, name="search-figure"),
    path("select_figure/", views.select_figure, name="select-figure"),
    path(
        "select_image/",
        views.select_image,
        name="select-image",
    ),
    # path("battle_screen/",views.)
]
