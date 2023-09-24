from django.db import models
from django.utils import timezone


class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Director(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Film(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateTimeField(default=timezone.now)
    created_in_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    director = models.ManyToManyField(Director)

    def __str__(self):
        return self.title


class Review(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField()
    review_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.review_text


class Poster(models.Model):
    film = models.OneToOneField(
        Film, on_delete=models.CASCADE, primary_key=True, related_name="poster"
    )
    image = models.ImageField(upload_to="posters/", blank=True, null=True)
    explanation_img = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.image.url
