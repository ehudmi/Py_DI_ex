from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    image = models.ImageField(upload_to="images/")
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return self.description[:50]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    number_images_uploaded = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
