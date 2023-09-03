from django.db import models


class Figure(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    image_url = models.URLField()


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    matches_played = models.IntegerField(default=0)
    matches_won = models.IntegerField(default=0)
    figures_played = models.ManyToManyField(Figure)
