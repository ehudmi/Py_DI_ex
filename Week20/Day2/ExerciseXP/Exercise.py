# 🌟 Exercise 1: Cats
# Instructions
# Using this class


class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


# Instantiate three Cat objects using the code provided above.
# Outside of the class, create a function that finds the oldest cat and returns the cat.
# Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function
# previously created.

cat_1 = Cat("Tommy", 2)
cat_2 = Cat("Bella", 10)
cat_3 = Cat("Jason", 5)


def find_oldest(*args):
    list_cats = [[i.name, i.age] for i in args]
    max_age = 0
    cat_name = ""
    for item in list_cats:
        if item[1] > max_age:
            max_age = item[1]
            cat_name = item[0]
    print(f"The oldest cat is {cat_name}, and is {max_age} years old.")


find_oldest(cat_1, cat_2, cat_3)

# 🌟 Exercise 2 : Dogs
# Instructions
# Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height. This function instantiates
# two attributes, which values are the parameters.
# Create a method called bark that prints the following string “<dog_name> goes woof!”.
# Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog (ie. name and height) and call the methods bark and jump.
# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog (ie. name and height) and call the methods bark and jump.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.


class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height*2} cm high!")


davids_dog = Dog("Rex", 50)

print(f"David has a dog named {davids_dog.name}. It's {davids_dog.height} cm tall")
Dog.bark(davids_dog)
Dog.jump(davids_dog)

sarahs_dog = Dog("Teacup", 20)

print(f"David has a dog named {sarahs_dog.name}. It's {sarahs_dog.height} cm tall")
Dog.bark(sarahs_dog)
Dog.jump(sarahs_dog)


if davids_dog.height > sarahs_dog.height:
    print(f"David's dog is bigger")
else:
    print(f"Sarah's dog is bigger")

# 🌟 Exercise 3 : Who’s The Song Producer?
# Instructions
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
# Create an object, for example:

# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])


class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        [print(f"{item}") for item in self.lyrics]


stairway = Song(
    [
        "There’s a lady who's sure",
        "all that glitters is gold",
        "and she’s buying a stairway to heaven",
    ]
)

Song.sing_me_a_song(stairway)
# Then, call the sing_me_a_song method. The output should be:

# There’s a lady who's sure
# all that glitters is gold
# and she’s buying a stairway to heaven


# Exercise 4 : Afternoon At The Zoo
# Instructions
# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the
# animals list as long as it isn’t already in the list.
# Create a method called get_animals that prints all the animals of the zoo.
# Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from
# the list and of course the animal needs to exist in the list.
# Create a method called sort_animals that sorts the animals alphabetically and groups them together based on
# their first letter.
# Example


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        return self.animals

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        return self.animals

    def sort_animals(self):
        self.animals_dict = {}
        self.animals_sorted = sorted(self.animals)
        counter = 1
        item_list = []
        for item in self.animals_sorted:
            if len(item_list) == 0:
                self.animals_dict.update({int(counter): item})
                item_list.append(item)
            elif str(item)[0] == item_list[-1][0]:
                item_list.append(item)
                self.animals_dict.update({int(counter): item_list.copy()})
            else:
                counter += 1
                item_list.clear()
                self.animals_dict.update({int(counter): item})
                item_list.append(item)

    def get_groups(self):
        self.sort_animals()
        for k in self.animals_dict.keys():
            print(self.animals_dict[k])


# {
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }


# Create a method called get_groups that prints the animal/animals inside each group.

# Create an object called ramat_gan_safari and call all the methods.
# Tip: The zookeeper is the one who will use this class.
# Example
# Which animal should we add to the zoo --> Giraffe
# x.add_animal(Giraffe)

ramat_gan_safari = Zoo("ramat_gan")

ramat_gan_safari.add_animal("Ape")
ramat_gan_safari.add_animal("Baboon")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Cat")
ramat_gan_safari.add_animal("Cougar")
ramat_gan_safari.add_animal("Eel")
ramat_gan_safari.add_animal("Emu")

ramat_gan_safari.get_groups()
