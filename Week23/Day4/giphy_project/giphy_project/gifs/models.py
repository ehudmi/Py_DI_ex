from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField()

    def __str__(self) -> str:
        return self.name


class Gif(models.Model):
    title = models.CharField()
    url = models.URLField()
    uploader_name = models.CharField()
    created_at = models.DateTimeField(default=timezone.now)
    categories = models.ManyToManyField(Category, related_name="gifs")
    likes = models.IntegerField(default=0)
