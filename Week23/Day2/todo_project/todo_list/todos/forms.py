from django import forms
from .models import Category, Todo


class ToDoForm(forms.ModelForm):
    date_creation = forms.DateField(input_formats=["%d/%m/%Y"])
    date_completion = forms.DateField(input_formats=["%d/%m/%Y"])
    deadline_date = forms.DateField(input_formats=["%d/%m/%Y"])
    widgets = {
        "text": forms.Textarea(attrs={"class": "textarea"}),
        "category": forms.ModelChoiceField(queryset=Category.objects.all()),
    }

    class Meta:
        model = Todo
        fields = "__all__"
