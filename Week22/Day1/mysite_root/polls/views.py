from django.shortcuts import render  # this line is added automatically
from django.http import HttpResponse  # pass view information into the browser


# takes a request, returns a response
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def about(request):
    return HttpResponse("<h1> Welcome Users<h1>")


# def about(request):
#     context = get_data(...) # fetch the data you need
#     return render(request, "myapp/template/about.html", context)
