from django import forms
from .models import User, Figure


class Signup(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"


class Figures(forms.ModelForm):
    class Meta:
        model = Figure
        fields = "__all__"