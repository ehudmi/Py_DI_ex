from django import forms
from .models import Film, Director, Review, Category, Poster


class FilmForm(forms.ModelForm):
    release_date = forms.DateField(
        widget=forms.DateInput(format="%d/%m/%Y"), input_formats=["%d/%m/%Y"]
    )
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all().order_by("name"),
        label="Categories",
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Film
        fields = "__all__"


class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = "__all__"


class ReviewForm(forms.ModelForm):
    CHOICES = [
        (1, "Terrible"),
        (2, "Meh"),
        (3, "Average"),
        (4, "Good"),
        (5, "Excellent"),
    ]
    review_date = forms.DateField(
        widget=forms.DateInput(format="%d/%m/%Y"), input_formats=["%d/%m/%Y"]
    )
    rating = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES,
    )
    widgets = {
        "text": forms.Textarea(attrs={"class": "textarea"}),
    }

    class Meta:
        model = Review
        fields = "__all__"


class PosterForm(forms.ModelForm):
    class Meta:
        model = Poster
        fields = "__all__"
