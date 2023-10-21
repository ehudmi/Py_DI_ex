from django.db import models
from random import randint


class User(models.Model):
    username = models.CharField(unique=True)
    email = models.EmailField(unique=True)
    amount_of_money = models.IntegerField(default=1000)
    points = models.IntegerField(default=0)


class Card(models.Model):
    id = models.CharField(primary_key=True)
    name_character = models.CharField()
    species = models.CharField()
    house = models.CharField()
    image_url = models.CharField()
    date_of_birth = models.CharField()
    patronus = models.CharField()
    price = models.IntegerField(default=randint(200, 2000))
    xp_points = models.IntegerField(default=randint(1, 10))
    current_owner = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="current"
    )
    previous_owner = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="previous"
    )
