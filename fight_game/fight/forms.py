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


class SearchFigure(forms.Form):
    name = forms.CharField(max_length=100, required=False)
    occupation = forms.CharField(max_length=100, required=False)


class Figures(forms.ModelForm):
    class Meta:
        model = Figure
        fields = "__all__"
