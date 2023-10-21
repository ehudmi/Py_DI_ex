from django.forms import ModelForm
from .models import Image, Album


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ["image", "description", "album"]


class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = ["title", "description"]
