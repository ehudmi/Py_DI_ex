from django.shortcuts import render
from django.db.models import Q
from .models import Gif
from .forms import GifSearchForm


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
        print(gifs.count())
        context = {"form": form, "gifs": gifs}
        return render(request, "gifs/homepage.html", context)
