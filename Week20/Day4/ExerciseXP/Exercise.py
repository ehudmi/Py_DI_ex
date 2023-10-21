# 🌟 Exercise 1 : Pets
# Instructions
# Using this code:


class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f"{self.name} is just walking around"


class Bengal(Cat):
    def sing(self, sounds):
        return f"{sounds}"


class Chartreux(Cat):
    def sing(self, sounds):
        return f"{sounds}"


# Create another cat breed named Siamese which inherits from the Cat class.
# Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
# Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class,
# and pass the variable all_cats to the new instance.
# Take all the cats for a walk, use the walk method.


class Siamese(Cat):
    def play(self):
        pass


all_cats = [Bengal("Suzie", 5), Chartreux("Tommy", 3), Siamese("Jack", 1)]
sara_pets = Pets(all_cats)

sara_pets.walk()

# 🌟 Exercise 2 : Dogs
# Instructions
# Create a class called Dog with the following attributes name, age, weight.
# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.
# run_speed: returns the dogs running speed (weight/age*10).
# fight : takes a parameter which value is another Dog instance, called other_dog.
# This method returns a string stating which dog won the fight. The winner should be the dog with
# the higher run_speed x weight.

# Create 3 dogs and run them through your class.


# class Dog:
#     def __init__(self, name, age, weight):
#         self.name = name
#         self.age = age
#         self.weight = weight

#     def bark(self):
#         return f"{self.name} is barking"

#     def run_speed(self):
#         return self.weight / self.age * 10

#     def fight(self, other_dog):
#         if self.run_speed() > other_dog.run_speed():
#             return self.run_speed()
#         else:
#             return other_dog.run_speed()


# dogs = [Dog("Rex", 5, 10), Dog("Caesar", 3, 15), Dog("Max", 2, 40)]
# for item in dogs:
#     print(item.bark())
#     print(item.run_speed())
# for i in range(0, 3):
#     if i == 0:
#         print(dogs[i].fight(dogs[i + 1]))
#         print(dogs[i].fight(dogs[i + 2]))
#     if i == 1:
#         print(dogs[i].fight(dogs[i + 1]))


# 🌟 Exercise 3 : Dogs Domesticated
# Instructions
# Create a new python file and import your Dog class from the previous exercise.
# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be
# False by default.
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True

# play: takes a parameter which value is a few names of other Dog instances (use *args).
# The method should print the following string: “dog_names all play together”.

# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.

from random import randint
from doggy import Dog


class PetDog(Dog):
    # def __init__(self, name, age, weight):
    #     self.trained = False
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(*args):
        print(f"{args} all play together")

    def doa_a_trick(self):
        tricks = [
            "does a barrel roll",
            "stands on his back legs",
            "shakes your hand",
            "plays dead",
        ]
        if self.trained == True:
            print(f"{self.name} {tricks[randint(0,3)]}")


dogs_1 = [PetDog("Rex", 5, 10), PetDog("Caesar", 3, 15), PetDog("Max", 2, 40)]

# for item in dogs_1:
#     item.train()
#     item.doa_a_trick()
