from django.shortcuts import render
from .models import Family, Animal

# from .read_data import (
#     get_all_animals,
#     get_all_families,
#     get_animals_per_family,
#     get_one_animal,
# )

# from .data import animals, families


# Create your views here.
# context = {"animals": animals, "families": families}


def display_all_animals(request):
    # return render(request, "animals/all_animals.html", {"animals": get_all_animals()})
    return render(
        request,
        "animals/all_animals.html",
        {"animals": sorted(Animal.objects.all(), key=lambda x: x.name)},
    )


def display_all_families(request):
    # return render(
    #     request, "animals/all_families.html", {"families": get_all_families()}
    # )
    return render(
        request,
        "animals/all_families.html",
        {"families": sorted(Family.objects.all(), key=lambda x: x.pk)},
    )


def display_one_animal(request, animal_id):
    # return render(
    #     request,
    #     "animals/animal.html",
    #     {"animal": get_one_animal(animal_id)},
    # )
    return render(
        request,
        "animals/animal.html",
        {"animal": Animal.objects.filter(id=animal_id).first()},
    )


def display_animal_per_family(request, family_id):
    # return render(
    #     request,
    #     "animals/animals_in_family.html",
    #     {"animals": get_animals_per_family(family_id)},
    # )
    return render(
        request,
        "animals/animals_in_family.html",
        {
            "animals": Animal.objects.filter(family_id=family_id),
            "counter": len(Animal.objects.filter(family_id=family_id)),
        },
    )


def display_animal_by_speed(request):
    return render(
        request,
        "animals/animal_by_speed.html",
        {"animals": sorted(Animal.objects.all(), key=lambda x: x.speed)},
    )
