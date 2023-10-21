from django.shortcuts import render
from .models import Person, Post

person = Person.objects.filter(first_name="Maria", last_name="Fez").first()
# get the first object because Person.objects.filter returns a QuerSet (ie. a list)


def index(request):
    context = {"page_title": "Homepage", "user": person}
    return render(request, "posts/homepage.html", context)


def posts(request):
    posts = Post.objects.filter(
        author__first_name=person.first_name, author__last_name=person.last_name
    )
    context = {"page_title": "Posts", "posts": posts}
    return render(request, "posts/posts.html", context)
