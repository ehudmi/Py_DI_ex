from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PersonForm
from .models import Person


def display_person_by_phonenumber(request, number):
    context = {"person": Person.objects.filter(phone=number).first()}
    return render(request, "search/person_by_number.html", context)


def display_person_by_name(request, name):
    context = {"person": Person.objects.filter(name=name).first()}
    return render(request, "search/person_by_name.html", context)


def add_person(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Person Added Successfully")
            return redirect("person", name=request.POST.get("name"))
        messages.error(request, "Error. Message not sent.")
    else:
        form = PersonForm()
    context = {"form": form}
    return render(request, "search/add_person.html", context)
