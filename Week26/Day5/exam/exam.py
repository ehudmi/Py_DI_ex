# Python Basics

# Data Types

# Which of the following is not a mutable data type in Python?
# a) List
# b) Dictionary
# c) Tuple - Immutable
# d) Set


# Lists and Loops

# Using a list comprehension, generate a list of the squares of numbers from 1 to 10, but only include
# squares of even numbers.

my_list = [x**2 for x in range(1, 11) if x % 2 == 0]

# Using the range function, create a list of numbers from 1 to 10, then print numbers that are
# divisible by both 2 and 3.

new_list = [x for x in range(1, 11) if x % 2 == 0 and x % 3 == 0]

# Loop through the provided list of dictionaries and print the names and ages:

student_list = [
    {"name": "John", "age": 24},
    {"name": "Anna", "age": 22},
    {"name": "Mike", "age": 25},
]

for student in student_list:
    print(student["name"], student["age"])

# Function Behavior with *args and **kwargs

# Write a function combine_words that accepts any number of positional arguments and key-value
# arguments. The function should return a single sentence combining all the words provided.
# Example:
# print(combine_words("Hello", "world", second="is", third="great!", first="Python"))
# Expected Output:

# "Hello world. Python is great!"


def combine_words(*args, **kwargs):
    return " ".join(args) + ". " + " ".join(kwargs.values()) + "!"


# Object-Oriented Programming (OOP)

# Create a class Vehicle with string attributes type, brand, and integer attribute year.
# Ensure instances of the vehicle cannot be created if any of these attributes are missing and
# include a method to display the vehicle’s info. Use dunder method.


class Vehicle:
    def __init__(self, type, brand, year):
        self.type = type
        self.brand = brand
        self.year = year

    def __str__(self):
        return f"{self.type} {self.brand} {self.year}"


# OOP Inheritance and Decorators

# Create a class Car with string attributes brand, model, and integer attribute mileage.
# Implement a method to return the car’s details.


class Car:
    def __init__(self, brand, model, mileage):
        self.brand = brand
        self.model = model
        self.mileage = mileage

    def details(self):
        return f"{self.brand} {self.model} {self.mileage}"


# Create a subclass ElectricCar inheriting from Car with an additional float private
# attribute __battery_capacity. Override the car’s details method to include the battery capacity.
# Use the @property decorator to get the battery_capacity value and @battery_capacity.setter to
# modify the battery capacity only if the new value is positive.


class ElectricCar(Car):
    def __init__(self, brand, model, mileage, battery_capacity):
        super().__init__(brand, model, mileage)
        self.__battery_capacity = battery_capacity

    def details(self):
        return f"{self.brand} {self.model} {self.mileage} {self.__battery_capacity}"

    @property
    def battery_capacity(self):
        return self.__battery_capacity

    @battery_capacity.setter
    def battery_capacity(self, new_capacity):
        if new_capacity > 0:
            self.__battery_capacity = new_capacity


# Create a BankAccount class with private float attribute _balance and private string
# attribute _account_holder. Implement methods to deposit, withdraw, and view the balance.
# Include a class method to track accounts created and a static method for a bank policy message.
# Ensure the balance is non-negative.


class BankAccount:
    __accounts_created = 0

    def __init__(self, account_holder, balance):
        self.__account_holder = account_holder
        self.__balance = balance
        BankAccount.__accounts_created += 1

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance - amount >= 0:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def view_balance(self):
        return self.__balance

    @classmethod
    def accounts_created(cls):
        return cls.__accounts_created

    @staticmethod
    def bank_policy():
        return "Bank policy message"


# Data Science

# Numpy and Pandas Visualization

# Create a numpy array of shape (3,3) filled with integers from 1 to 9 using arange().

import numpy as np

np.arange(1, 10).reshape(3, 3)


# Provided pandas DataFrame df:

import pandas as pd

df = pd.DataFrame({"A": [1, "apple", 3, 4, "banana"], "B": [5, 6, 7, 8, 9]})


# Replace non-numeric values in column “A” with the mean of numeric values.
# Plot a histogram of the “A” column using matplotlib.

# Plot “A” and “B” columns of df using matplotlib. Add x-axis, y-axis labels, and a title.

import matplotlib.pyplot as plt

df["A"] = pd.to_numeric(df["A"], errors="coerce")
df["A"].fillna(df["A"].mean(), inplace=True)
df["A"].plot(kind="hist")
plt.xlabel("A")
plt.ylabel("Frequency")
plt.title("A vs Frequency")
plt.show()


# Django and Django REST

# Create a new Django project called ‘academy’. After that - create a new app (inside the ‘academy’
# project) called ‘school’.


# Django Models with Foreign Key

# Define Django models Teacher and Course. Course has course_name (CharField) and course_code
# (CharField). Teacher has name (CharField). Create a many-to-many relationship between Teacher and
# Course.


# Views

# Create a Django view course_details to fetch details of a course by its id.


# Use a APIview for Teacher to display all teachers.


# Full App

# Create a base model SchoolFacility with facility_name (CharField) and usage_purpose (TextField).


# Create a Laboratory model inheriting from SchoolFacility with equipment_list (TextField).


# Create views for all school facilities and another for only laboratories.


# Create a serializer for SchoolFacility and another for Laboratory to convert to JSON. Test using
# Postman.
