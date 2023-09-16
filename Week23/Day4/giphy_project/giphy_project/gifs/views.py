from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Gif, Category
from .forms import GifSearchForm, CategoryForm


def display_gifs(request):
    if request.method == "POST":
        form = GifSearchForm(request.POST)
        if form.is_valid():
            search_term = request.POST.get("search_term")
            gifs = Gif.objects.filter(
                Q(title__icontains=search_term)
                | Q(categories__name__icontains=search_term)
            ).distinct()
            print(gifs.count())
            context = {"form": form, "gifs": gifs}
            return render(request, "gifs/homepage.html", context)
    else:
        form = GifSearchForm()
    gifs = Gif.objects.all()
    context = {"form": form, "gifs": gifs}
    return render(request, "gifs/homepage.html", context)


def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        context = {"form": form}
        if form.is_valid():
            form.save()
            messages.success(request, "Category Added Successfully")
            return render(request, "gifs/add_category.html", context)
        messages.error(request, "Error. Category not added.")

    form = CategoryForm()
    context = {"form": form}
    return render(request, "gifs/add_category.html", context)


def show_categories(request):
    categories = Category.objects.order_by("name").prefetch_related("gifs")
    context = {"categories": categories}
    return render(request, "gifs/list_categories.html", context)


def like_add(request, gif_id, counter):
    gif = Gif.objects.filter(id=gif_id).first()
    if gif is not None:
        if counter == 0:
            gif.likes -= 1
        else:
            gif.likes += 1
        gif.save()
    return redirect("display-gifs")


def sort_like(request):
    gifs = Gif.objects.filter(likes__gt=0).order_by("likes")
    context = {"gifs": gifs}
    return render(request, "gifs/like_gifs.html", context)
