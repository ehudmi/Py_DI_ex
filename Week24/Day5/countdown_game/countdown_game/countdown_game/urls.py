from django.contrib import admin
from django.urls import path, include
from .views import SignupView, LoginView, LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("countdown.urls")),
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
