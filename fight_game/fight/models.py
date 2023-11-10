from django.contrib.auth.models import AbstractUser
from django.db import models


class Figure(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100, null=True)
    notoriety = models.IntegerField(default=0)
    luck = models.IntegerField(default=0)
    num_images = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class FigureImage(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    image_url = models.URLField(max_length=500)
    figure = models.ForeignKey(Figure, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.figure.name} - {self.id}"


class FightUser(AbstractUser):
    matches_played = models.IntegerField(default=0)
    matches_won = models.IntegerField(default=0)
    figures_played = models.ManyToManyField(Figure)

    def __str__(self):
        return self.username


class Battle(models.Model):
    figure = models.ForeignKey(
        Figure, on_delete=models.CASCADE, related_name="figure", blank=True, null=True
    )
    image = models.ForeignKey(
        FigureImage,
        on_delete=models.CASCADE,
        related_name="image",
        blank=True,
        null=True,
    )
    player = models.ForeignKey(
        FightUser,
        on_delete=models.CASCADE,
        related_name="player",
        blank=True,
        null=True,
    )
    notoriety = models.IntegerField(default=0)
    intelligence = models.IntegerField(default=0)
    strength = models.IntegerField(default=0)
    luck = models.IntegerField(default=0)
    score = models.IntegerField(default=0)

    def __str__(self):
        if self.player is None and self.figure is not None:
            return f"Computer playing {self.figure.name}"
        elif self.player is not None and self.figure is not None:
            return f"{self.player.username} playing {self.figure.name}"
