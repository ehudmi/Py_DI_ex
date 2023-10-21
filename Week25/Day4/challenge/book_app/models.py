from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    page_count = models.IntegerField()
    categories = models.CharField(max_length=255)
    thumbnail_url = models.URLField(max_length=255)
    rating = models.FloatField(blank=True, null=True)


class BookReview(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField()
    review_text = models.TextField()
