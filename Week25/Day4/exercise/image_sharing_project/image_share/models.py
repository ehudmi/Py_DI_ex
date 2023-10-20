from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    image = models.ImageField(upload_to="images/")
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="images")
    album = models.ForeignKey(
        "Album", on_delete=models.CASCADE, related_name="images", null=True, blank=True
    )

    def __str__(self):
        return self.image.url


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    number_images_uploaded = models.IntegerField(default=0)
    number_following = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class Album(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="albums"
    )

    def __str__(self):
        return self.title


class Follow(models.Model):
    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="following"
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="followers"
    )

    def __str__(self):
        return f"{self.follower.username} follows {self.following.username}"
