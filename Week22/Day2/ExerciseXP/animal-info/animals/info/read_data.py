import json

dir_file = "C:/Github/Python_Bootcamp/Py_DI_ex/Week22/Day2/ExerciseXP/animal-info/animals/info/data.json"
with open(dir_file) as data_file:
    animals = json.load(data_file)


# return information about all the animals, as well as their family name.
def get_all_animals():
    return animals["animals"]


# return all the families name.
def get_all_families():
    return animals["families"]


#  return the information about one animal depending on its id.
def get_one_animal(animal_id):
    selected_animal = ""
    for animal in animals["animals"]:
        if animal["id"] == animal_id:
            selected_animal = animal
    return selected_animal


# return the information about all the animals from the particular family
def get_animals_per_family(family_id):
    selected_animals = []
    for animal in animals["animals"]:
        if animal["family"] == family_id:
            selected_animals.append(animal)
    return selected_animals
