from django import forms


class GifSearchForm(forms.Form):
    search_term = forms.CharField(max_length=50, required=False)
