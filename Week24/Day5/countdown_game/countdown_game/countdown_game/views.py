from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import views as auth_views


class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"


class LoginView(auth_views.LoginView):
    form_class = AuthenticationForm
    success_url = reverse_lazy("game")
    template_name = "login.html"


class LogoutView(TemplateView):
    success_url = reverse_lazy("login")
    template_name = "logout.html"
