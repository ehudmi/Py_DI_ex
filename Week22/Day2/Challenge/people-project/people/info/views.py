from django.shortcuts import render

# Create your views here.
name = "Bob Smith"
age = 35
country = "USA"

people = ["bob", "martha", "fabio", "john"]

all_people = [
    {"id": 1, "name": "Bob Smith", "age": 35, "country": "USA"},
    {"id": 2, "name": "Martha Smith", "age": 60, "country": "USA"},
    {"id": 3, "name": "Fabio Alberto", "age": 18, "country": "Italy"},
    {"id": 4, "name": "Dietrich Stein", "age": 85, "country": "Germany"},
]


def display_person(request):
    return render(
        request, "person.html", {"name": name, "age": age, "country": country}
    )


def display_people(request):
    return render(request, "people.html", {"people": sorted(people)})


def display_all_people(request):
    people_sorted = sorted(all_people, key=lambda x: x["age"])
    return render(request, "all_people.html", {"people": people_sorted})
