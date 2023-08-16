# 🌟 Exercise 1: Currencies
# Instructions
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        print(f"{self.amount} {self.currency}s")
        return self.currency

    def __int__(self):
        print(self.amount)
        return int(self.amount)

    def __repr__(self):
        # if isinstance(self, Currency):
        #     print(f"{self.amount} {self.currency}s")
        print(f"{self.amount} {self.currency}s")
        return self.currency

    def __add__(self, num2):
        if isinstance(num2, Currency):
            if self.currency != num2.currency:
                raise TypeError(
                    "Cannot add between Currency type <dollar> and <shekel>"
                )
            else:
                num2 = num2.amount
        print(self.amount + num2)
        return

    def __call__(self):
        print(self.amount)
        return self.amount

    # def __name__(self):
    #     print(f"{self.amount} {self.currency}s")
    #     return self.currency


# Using the code above, implement the relevant methods and dunder methods which will output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.
c1 = Currency("dollar", 5)
c2 = Currency("dollar", 10)
c3 = Currency("shekel", 1)
c4 = Currency("shekel", 10)

# str(c1)
# '5 dollars'

# int(c1)
# 5

# repr(c1)
# '5 dollars'

# c1 + 5
# 10

# c1 + c2
# 15

# c1()
# 5 dollars

# >>> c1 += 5
# >>> c1
# 10 dollars

# >>> c1 += c2
# >>> c1
# 20 dollars

# c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>


# 🌟 Exercise 2: Import
# Instructions
# In a file named func.py create a function that adds 2 number, and prints the result
# In a file namedexercise_one.py import and the function
# Hint: You can use the the following syntaxes:

# import module_name

# OR

# from module_name import function_name

# OR

# from module_name import function_name as fn

# OR

# import module_name as mn


# 🌟 Exercise 3: Random Module
# Instructions
# Create a function that accepts a number between 1 and 100, then rolls a random number between 1 and 100,
# if it’s the same number, display a success message to the user, else don’t.

import random
from typing import Any


def roll_num(num1):
    if num1 == random.randint(0, 100):
        print("Success")


# roll_num(76)


# 🌟 Exercise 4: String Module
# Instructions
# Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# Hint: use the string module

import string


def gen_string():
    result = "".join(random.choices(string.ascii_letters, k=5))
    print(result)


# gen_string()

# 🌟 Exercise 5 : Current Date
# Instructions
# Create a function that displays the current date.
# Hint : Use the datetime module.

import datetime


def display_now():
    print(
        f"{datetime.datetime.now().year}-{datetime.datetime.now().month}-{datetime.datetime.now().day}"
    )


# display_now()

# Exercise 6 : Amount Of Time Left Until January 1st
# Instructions
# Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st of January is in 10 days and 10:34:01hours).


def time_to_newyear():
    secs_in_a_day = 86400
    secs_in_a_hour = 3600
    secs_in_a_min = 60

    today = datetime.datetime.now()
    newyear_date = datetime.datetime(2024, 1, 1)
    delta = newyear_date - today
    seconds = int(delta.total_seconds())

    days, seconds = divmod(seconds, secs_in_a_day)
    hours, seconds = divmod(seconds, secs_in_a_hour)
    minutes, seconds = divmod(seconds, secs_in_a_min)

    time_fmt = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    print(f"the 1st of January is in {days} days and {time_fmt}")


# time_to_newyear()

# Exercise 7 : Birthday And Minutes
# Instructions
# Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message
# stating how many minutes the user lived in his life.


def live_long(birthdate):
    secs_in_a_day = 86400
    secs_in_a_hour = 3600
    secs_in_a_min = 60

    format = "%d/%m/%Y"
    birthdate = datetime.datetime.strptime(birthdate, format)
    today = datetime.datetime.now()
    delta = today - birthdate
    seconds = int(delta.total_seconds())

    hours, seconds = divmod(seconds, secs_in_a_hour)
    minutes, seconds = divmod(seconds, secs_in_a_min)

    time_fmt = f"{hours:02d}"
    print(f"You have lived {time_fmt} hours")


# live_long("03/12/1966")

# Exercise 8 : Faker Module
# Instructions
# Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
# Create an empty list called users. Tip: It should be a list of dictionaries.
# Create a function that adds new dictionaries to the users list. Each user has the following keys: name, address,
# language_code. Use faker to populate them with fake data.

from faker import Faker

users = []


def populate_users():
    fake = Faker()
    users.append(
        {"name": fake.name(), "address": fake.address(), "language_code": fake.locale()}
    )
    return users


# populate_users()
# print(users)
