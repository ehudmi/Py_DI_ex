from django.urls import path
from .views import (
    SignUpView,
    HomeView,
    # get_figure,
    # get_image,
    search_figure,
    after_select_figure,
    get_images,
    after_select_image,
    create_opponent_by_name,
    create_opponent_by_occupation,
    BattleView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("signup/", SignUpView.as_view(), name="signup"),
    # path("get_figure/", get_figure, name="get-figure"),
    # path("get_image/", get_image, name="get-image"),
    path("search_figure/", search_figure, name="search-figure"),
    path("selected_figure/", after_select_figure, name="selected-figure"),
    path("get_images/<id>", get_images, name="get-images"),
    path(
        "selected_image/<id>",
        after_select_image,
        name="selected-image",
    ),
    path("create_opponent_by_name/", create_opponent_by_name, name="create-opponent"),
    path(
        "create_opponent_by_occupation/",
        create_opponent_by_occupation,
        name="create-opponent-occupation",
    ),
    path("battle/", BattleView.as_view(), name="battle"),
]
