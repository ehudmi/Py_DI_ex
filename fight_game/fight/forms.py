from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import FightUser, Figure


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = FightUser
        fields = ("username", "email")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = FightUser
        fields = ("username", "email")


class Figures(forms.ModelForm):
    class Meta:
        model = Figure
        fields = "__all__"
