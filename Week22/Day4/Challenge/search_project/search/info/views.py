from django.shortcuts import render
from .models import Person


def display_person_by_phonenumber(request, number):
    context = {"person": Person.objects.filter(phone=number).first()}
    return render(request, "search/person_by_number.html", context)


def display_person_by_name(request, name):
    context = {"person": Person.objects.filter(name=name).first()}
    return render(request, "search/person_by_name.html", context)
