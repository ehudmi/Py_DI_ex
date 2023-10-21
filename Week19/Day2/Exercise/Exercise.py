# Exercise 1 : What Are You Learning ?
# Instructions
# Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# Call the function, and make sure the message displays correctly.


def display_message(learn_item):
    print(f"I am learning {learn_item}")


display_message("Python")

# 🌟 Exercise 2: What’s Your Favorite Book ?
# Instructions
# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as "One of my favorite books is <title>".
# For example: “One of my favorite books is Alice in Wonderland”
# Call the function, make sure to include a book title as an argument when calling the function.


def favorite_book(title):
    print(f"One of my favorite books is {title}")


favorite_book("Catch-22")

# 🌟 Exercise 3 : Some Geography
# Instructions
# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as "<city> is in <country>".
# For example “Reykjavik is in Iceland”
# Give the country parameter a default value.
# Call your function.


def describe_city(city, country):
    print(f"{city} is in {country}")


describe_city("Reykjavik", "Iceland")

# Exercise 4 : Random
# Instructions
# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.

from random import randint


def gen_random(user_number):
    comp_number = randint(1, 100)
    if user_number == comp_number:
        print(
            f"Success - your number was {user_number} and the computer selected {comp_number}"
        )
    else:
        print(
            f"Fail- your number was {user_number} and the computer selected {comp_number}"
        )


gen_random(int(input("give me a number between 1 and 100 ")))

# 🌟 Exercise 5 : Let’s Create Some Personalized Shirts !
# Instructions
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
# Call the function make_shirt().

# Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
# Make a large shirt with the default message
# Make medium shirt with the default message
# Make a shirt of any size with a different message.

# Bonus: Call the function make_shirt() using keyword arguments.


def make_shirt(size, text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}")


make_shirt(size="large")
make_shirt(size="medium")
make_shirt(text="I love Javascript", size=input("What size shirt would you like? "))


# 🌟 Exercise 6 : Magicians …
# Instructions
# Using this list of magician’s names.
magician_names = ["Harry Houdini", "David Blaine", "Criss Angel"]
# Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
# Call the function make_great().
# Call the function show_magicians() to see that the list has actually been modified.


def show_magicians():
    for item in magician_names:
        print(item)


def make_great():
    counter = 0
    for item in magician_names:
        item = f"{item} the Great"
        magician_names[counter] = item
        counter += 1


make_great()
show_magicians()
