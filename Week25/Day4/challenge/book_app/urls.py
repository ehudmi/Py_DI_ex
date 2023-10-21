from django.urls import path
from .views import (
    IndexView,
    BookDetailView,
    MyBookReviewView,
    BookSearchView,
    AddBookReviewView,
    UpdateBookReviewView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("book/<str:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("my_reviews/", MyBookReviewView.as_view(), name="my-reviews"),
    path("book_search/", BookSearchView.as_view(), name="search-book"),
    path("add_review/<str:pk>/", AddBookReviewView.as_view(), name="add-review"),
    path(
        "update_review/<str:pk>/",
        UpdateBookReviewView.as_view(),
        name="update-review",
    ),
]
