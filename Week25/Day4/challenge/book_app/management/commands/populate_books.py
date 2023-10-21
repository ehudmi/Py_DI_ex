from django.core.management.base import BaseCommand
import requests
from book_app.models import Book


class Command(BaseCommand):
    help = "Populates the Books model with data from the Google Books API"

    def handle(self, *args, **kwargs):
        API_URL = "https://www.googleapis.com/books/v1/volumes?q=magic&maxResults=40"
        response = requests.get(API_URL)
        if response.status_code != 200:
            self.stdout.write(
                self.style.ERROR("Failed to fetch data from Google Books API")
            )
            return

        books = response.json()

        Book.objects.all().delete()

        for book in books["items"]:
            id = book.get("id", "")
            title = book["volumeInfo"].get("title", "")
            author = book["volumeInfo"].get("authors", "")
            published_date = book["volumeInfo"].get("publishedDate", "")
            description = book["volumeInfo"].get("description", "")
            page_count = book["volumeInfo"].get("pageCount", 0)
            categories = book["volumeInfo"].get("categories", "")
            thumbnail = book["volumeInfo"].get("imageLinks", "")
            thumbnail_url = thumbnail.get("thumbnail", "")

            if len(published_date) < 5:
                published_date = f"{published_date}-01-01"
            if len(published_date) < 8:
                published_date = f"{published_date}-01"

            book = Book(
                id,
                title,
                author,
                published_date,
                description,
                page_count,
                categories,
                thumbnail_url,
            )
            book.save()

        self.stdout.write(
            self.style.SUCCESS("Successfully populated books from the Google Books API")
        )
