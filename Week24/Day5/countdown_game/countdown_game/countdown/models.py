from django.db import models
from django.contrib.auth.models import User


class HighScore(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.player} - {self.score}"


class Word(models.Model):
    word_text = models.CharField(max_length=50)
    word_length = models.IntegerField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.word_text}"


class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    current_word = models.CharField(max_length=50, default="")
    shuffled_word = models.CharField(max_length=50, default="")
    num_guesses = models.IntegerField(default=3)
    current_score = models.IntegerField(default=0)
    current_message = models.CharField(max_length=50, default="")

    def __str__(self):
        return f"{self.user} - {self.current_score} - {self.current_word}"
