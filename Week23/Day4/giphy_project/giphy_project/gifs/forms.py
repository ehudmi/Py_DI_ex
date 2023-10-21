from django import forms
from .models import Category


class GifSearchForm(forms.Form):
    search_term = forms.CharField(max_length=50, required=False)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
