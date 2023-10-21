from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, View, UpdateView
from django.db.models import Avg, Count
from .models import Book, BookReview
from .forms import SearchBook, BookReviewForm


class IndexView(ListView):
    model = Book
    template_name = "index.html"
    context_object_name = "books"


class BookDetailView(DetailView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "data"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["book"] = Book.objects.get(pk=self.kwargs["pk"])
        reviews = BookReview.objects.filter(book=context["book"])
        context["reviews"] = reviews
        context["avg_rating"] = reviews.aggregate(Avg("rating"))["rating__avg"]
        context["num_reviews"] = reviews.aggregate(Count("rating"))["rating__count"]
        return context


class MyBookReviewView(ListView):
    model = BookReview
    template_name = "reviews/my_reviews.html"
    context_object_name = "reviews"

    def get_queryset(self):
        return BookReview.objects.filter(user=self.request.user)


class BookSearchView(View):
    def get(self, request):
        form = SearchBook()
        return render(request, "books/book_search.html", {"form": form})

    def post(self, request):
        form = SearchBook(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            author = form.cleaned_data["author"]
            books = Book.objects.filter(
                title__icontains=title, author__icontains=author
            )
            return render(
                request, "books/book_search.html", {"form": form, "books": books}
            )
        return render(request, "books/book_search.html", {"form": form})


class AddBookReviewView(View):
    def post(self, request, pk):
        form = BookReviewForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data["rating"]
            review_text = form.cleaned_data["review_text"]
            book = Book.objects.get(pk=pk)
            review = BookReview(
                book=book, user=request.user, rating=rating, review_text=review_text
            )
            review.save()
            return redirect("book-detail", pk=pk)
        return render(request, "reviews/add_review.html", {"form": form})

    def get(self, request, pk):
        form = BookReviewForm()
        return render(request, "reviews/add_review.html", {"form": form})


class UpdateBookReviewView(UpdateView):
    model = BookReview
    template_name = "reviews/update_review.html"
    fields = ["rating", "review_text"]
    context_object_name = "review"
    pk_url_kwarg = "review_pk"

    def get_success_url(self):
        return reverse("book-detail", kwargs={"pk": self.kwargs["pk"]})

    def get_queryset(self):
        return BookReview.objects.filter(user=self.request.user)
