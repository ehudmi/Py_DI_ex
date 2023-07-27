# 🌟 Exercise 1 : Set
# Instructions
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

my_set = {3, 6, 12}
my_set.add(24)
my_set.add(36)
print(my_set)
my_set.remove(24)
print(my_set)
friend_fav_numbers = set({2, 7, 9})
our_fav_numbers = my_set.union(friend_fav_numbers)
print(our_fav_numbers)


# 🌟 Exercise 2: Tuple
# Instructions
# Given a tuple which value is integers, is it possible to add more integers to the tuple?

# no - a tuple is immutable


# 🌟 Exercise 3: List
# Instructions
# Using this list
basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)

basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
print(basket.count("Apples"))
basket.clear()
print(basket)

# 🌟 Exercise 4: Floats
# Instructions
# Recap – What is a float? What is the difference between an integer and a float?
# Can you think of another way to generate a sequence of floats?
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).

# The difference between an integer and a float is the decimal point and option to use fractions

my_int_list = list(range(3, 11))
my_list = []
for i in my_int_list:
    my_list.append(i / 2)
print(my_list)

# 🌟 Exercise 5: For Loop
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

num_list = list(range(0, 21))
for item in num_list:
    print(item)
for item in num_list:
    if num_list.index(item) % 2 == 0:
        print(item)


# 🌟 Exercise 6 : While Loop
# Instructions
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.

my_name = "ehud"
user_name = ""
while user_name != my_name:
    user_name = input("What is your name? ")


# 🌟 Exercise 7: Favorite Fruits
# Instructions
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

user_fav_fruits = input(
    "What are your favorite fruits? please place a space between each fruit "
)
user_fruit_list = list(user_fav_fruits.split(" "))
user_new_fruit = input("add another fruit ")
if user_new_fruit in user_fruit_list:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")


# Exercise 8: Who Ordered A Pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

topping_list = list()
new_topping = ""
pizza_price = 10
while new_topping != "quit":
    new_topping = input("Please select a topping for the pizza ")
    if new_topping == "quit":
        break
    print(f"I will add {new_topping} to the pizza")
    topping_list.append(new_topping)
    pizza_price += 2.5
print(
    f"You have selected for the pizza the toppings: {', '.join(topping_list)} and the total cost is ${pizza_price}"
)


# Exercise 9: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Ask a family the age of each person who wants a ticket.

# Store the total cost of all the family’s tickets and print it out.

# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.

counter = 0
total_price = 0
family_members_num = input("How many members in your family? ")
while counter < int(family_members_num):
    age = int(input("What is the age of the family member? "))
    if age < 3:
        ticket_price = 0
    elif 3 <= age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15
    total_price += ticket_price
    counter += 1
print(total_price)

name_list = ["Ehud", "Moshe", "Haim", "Asher"]
allowed_list = name_list.copy()
for item in name_list:
    age = int(input(f"{item} - How old are you? "))
    if age > 21 or age < 16:
        allowed_list.remove(item)
print(allowed_list)


# Exercise 10 : Sandwich Orders
# Instructions
# Using the list below :

sandwich_orders = [
    "Tuna sandwich",
    "Pastrami sandwich",
    "Avocado sandwich",
    "Pastrami sandwich",
    "Egg sandwich",
    "Chicken sandwich",
    "Pastrami sandwich",
]

# The deli has run out of pastrami, use a while loop to remove all occurrences of “Pastrami sandwich” from sandwich_orders.
# We need to prepare the orders of the clients:
# Create an empty list called finished_sandwiches.
# One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
# After all the sandwiches have been made, print a message listing each sandwich that was made, such as:
# I made your tuna sandwich
# I made your avocado sandwich
# I made your egg sandwich
# I made your chicken sandwich

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
print(sandwich_orders)
finished_orders = list()
while len(sandwich_orders) > 0:
    finished_orders.append(sandwich_orders[0])
    sandwich_orders.pop(0)
for item in finished_orders:
    print(f"I made your {item}")
