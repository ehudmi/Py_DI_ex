from django.contrib.auth.models import AbstractUser
from django.db import models


class Figure(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100, null=True)
    image_url = models.URLField()


class FightUser(AbstractUser):
    matches_played = models.IntegerField(default=0)
    matches_won = models.IntegerField(default=0)
    figures_played = models.ManyToManyField(Figure)

    def __str__(self):
        return self.username
