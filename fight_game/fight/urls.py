from django.urls import path
from .views import (
    SignUpView,
    HomeView,
    search_figure,
    after_select_figure,
    get_images,
    after_select_image,
    create_opponent_by_name,
    create_opponent_by_occupation,
    BattleView,
    OutcomeView,
    cleanup,
    ProfileView,
    ProfileFigureView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("signup/", SignUpView.as_view(), name="signup"),
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
        "create_opponent_by_occupation/<id>",
        create_opponent_by_occupation,
        name="create-opponent-occupation",
    ),
    path("battle/", BattleView.as_view(), name="battle"),
    path("outcome/", OutcomeView.as_view(), name="outcome"),
    path("cleanup/", cleanup, name="cleanup"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile_figure/<pk>", ProfileFigureView.as_view(), name="profile-figure"),
]
