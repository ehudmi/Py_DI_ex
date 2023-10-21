from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import BookReview
from django.db.models import Avg


@receiver(post_save, sender=BookReview)
def update_book_rating(sender, instance, created, **kwargs):
    if created:
        book = instance.book
        reviews = BookReview.objects.filter(book=book)
        book.rating = reviews.aggregate(Avg("rating"))["rating__avg"]
        book.save()
