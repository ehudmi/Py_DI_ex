from django.db import models
from films.models import Film
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_films = models.ManyToManyField(Film)

    def __str__(self):
        return self.user.username
