# from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

# from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from .forms import SignUpForm, LoginForm


# class SignupView(CreateView):
#     form_class = SignUpForm
#     success_url = reverse_lazy("login")
#     template_name = "accounts/register.html"
def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        user = authenticate(
            request,
            username=request.POST.get("username"),
            password=request.POST.get("password"),
        )
        if user is not None:
            login(request, user)
        else:
            user = form.save()
    else:
        form = SignUpForm()
    context = {"form": form}
    return render(request, "accounts/register.html", context)


# class UserLoginView(LoginView):
#     form_class = LoginForm
#     template_name = "accounts/login.html"
def log_in_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        user = authenticate(
            request,
            username=request.POST.get("username"),
            password=request.POST.get("password"),
        )
        if user is not None:
            login(request, user)
            return redirect("homepage")
        else:
            return redirect("signup")
    else:
        form = LoginForm()
    context = {"form": form}
    return render(request, "accounts/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("homepage")


def profile(request, user_id):
    user = User.objects.get(id=user_id)
    context = {"user": user}
    return render(request, "accounts/profile.html", context)
