from django.contrib.auth.models import User
from django.db import models

CATEGORY_CHOICES = (
    ("Dj", "Django"),
    ("Py", "Python"),
)


class Comment(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    custom_id = models.IntegerField()
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES)
    comments = models.ManyToManyField(Comment)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
