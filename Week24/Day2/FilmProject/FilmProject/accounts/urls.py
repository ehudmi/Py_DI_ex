from django.urls import path
from .views import signup_view, log_in_view, profile, logout_view

urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("login/", log_in_view, name="login"),
    path("profile/<int:user_id>/", profile, name="profile"),
    path("logout/", logout_view, name="logout"),
]
