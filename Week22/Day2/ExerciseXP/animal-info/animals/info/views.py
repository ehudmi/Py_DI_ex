from django.shortcuts import render
from .data import animals, families


# Create your views here.
# context = {"animals": animals, "families": families}


def display_all_animals(request):
    return render(request, "animals/all_animals.html", {"animals": animals})


def display_all_families(request):
    return render(request, "animals/all_families.html", {"families": families})


def display_one_animal(request, animal_id):
    selected_animal = "horse"
    for animal in animals:
        if animal["id"] == animal_id:
            selected_animal = animal
    return render(
        request,
        "animals/animal.html",
        {"animal": selected_animal},
    )


def display_animal_per_family(request, family_id):
    selected_animals = []

    for animal in animals:
        if animal["family"] == family_id:
            selected_animals.append(animal)
    return render(
        request,
        "animals/animals_in_family.html",
        {"animals": selected_animals},
    )
