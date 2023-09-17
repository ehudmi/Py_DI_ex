from django import forms
from .models import Film, Director


class FilmForm(forms.ModelForm):
    release_date = forms.DateField(input_formats=["%d/%m/%Y"])

    class Meta:
        model = Film
        fields = "__all__"


class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = "__all__"
