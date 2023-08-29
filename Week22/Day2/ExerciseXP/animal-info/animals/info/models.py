from django.db import models


class Family(models.Model):
    name = models.CharField()


class Animal(models.Model):
    name = models.CharField()
    legs = models.IntegerField()
    weight = models.DecimalField(decimal_places=2, max_digits=10)
    height = models.DecimalField(decimal_places=2, max_digits=10)
    speed = models.DecimalField(decimal_places=2, max_digits=10)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
