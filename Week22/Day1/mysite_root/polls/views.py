from django.shortcuts import render  # this line is added automatically

# takes a request, returns a response
user = {"first_name": "John", "last_name": "Doe"}


# index function renders homepage.html template
def index(request):
    context = {
        "page_title": "Homepage",
        "user": user,
    }
    return render(request, "posts/homepage.html", context)


# posts function renders posts.html template
def posts(request):
    subjects = [
        {"title": "How to setup Django", "author": "Maria"},
        {"title": "How to cake an amazing pie", "author": "Chef Mark"},
    ]

    context = {"page_title": "Posts", "user": user, "subjects": subjects}

    return render(request, "posts/posts.html", context)
