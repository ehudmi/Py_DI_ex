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

    review_text = forms.CharField(widget=forms.Textarea(attrs={"class": "textarea"}))
    rating = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES,
    )
    review_date = forms.DateField(
        widget=forms.DateInput(format="%d/%m/%Y"), input_formats=["%d/%m/%Y"]
    )

    class Meta:
        model = Review
        fields = ["film", "review_text", "rating", "review_date"]


class PosterForm(forms.ModelForm):
    class Meta:
        model = Poster
        fields = "__all__"
