from django.forms import ModelForm
from .models import Image, Profile


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ["image", "description"]
