from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column
from .models import Film, Director, Review, Category, Poster, Producer


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
    explanation_img = forms.CharField(
        widget=forms.Textarea(attrs={"class": "textarea"})
    )

    class Meta:
        model = Poster
        fields = "__all__"


class ProducerForm(forms.ModelForm):
    class Meta:
        model = Producer
        fields = ["first_name", "last_name"]


class ProducerFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(ProducerFormHelper, self).__init__(*args, **kwargs)
        self.layout = Layout(
            Row(
                Column(("first_name"), css_class="col-md-6"),
                Column(("last_name"), css_class="col-md-6"),
                css_class="form-row",
            )
        )
