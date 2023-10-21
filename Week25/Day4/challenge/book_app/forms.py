from django import forms
from .models import BookReview


class SearchBook(forms.Form):
    title = forms.CharField(max_length=100, required=False)
    author = forms.CharField(max_length=100, required=False)


class BookReviewForm(forms.ModelForm):
    CHOICES = [(1, "⭐"), (2, "⭐" * 2), (3, "⭐" * 3), (4, "⭐" * 4), (5, "⭐" * 5)]
    rating = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = BookReview
        fields = ["rating", "review_text"]
