from django import forms
from .models import Todo


class ToDoForm(forms.ModelForm):
    widgets = {
        "text": forms.Textarea(attrs={"class": "textarea"}),
    }

    class Meta:
        model = Todo
        fields = "__all__"
