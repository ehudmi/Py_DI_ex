# Exercise 1: Birthday Look-Up
# Instructions
# Create a variable called birthdays. Its value should be a dictionary.
# Initialize this variable with birthdays of 5 people of your choice. For each entry in the dictionary, the key should be the person’s name, and the value should be their birthday. Tip : Use the format “YYYY/MM/DD”.
# Print a welcome message for the user. Then tell them: “You can look up the birthdays of the people in the list!”“
# Ask the user to give you a person’s name and store the answer in a variable.
# Get the birthday of the name provided by the user.
# Print out the birthday with a nicely-formatted message.

birthdays = {
    "Ehud": "1966/12/03",
    "Moshe": "1966/11/17",
    "Jim": "1952/08/23",
    "Sarah": "1990/06/15",
    "Jane": "1930/03/03",
}
# print("Hello user. You can check out the birthdays for the list members")
# selected_name = input(
#     f"Please select one of the names on the list {' '.join(list(birthdays.keys()))} "
# )
# print(
#     f"Wish a happy birthday to {selected_name} who was born on {birthdays.get(selected_name)}"
# )


# Exercise 2: Birthdays Advanced
# Instructions
# Before asking the user to input a person’s name print out all of the names in the dictionary.
# If the person that the user types is not found in the dictionary, print an error message (“Sorry, we don’t have the birthday information for <person’s name>”)

# print("Hello user. You can check out the birthdays for the list members")
# selected_name = input(
#     f"Please select one of the names on the list {' '.join(list(birthdays.keys()))} "
# )
# if birthdays.get(selected_name) == None:
#     print(f"Sorry, we don’t have the birthday information for {selected_name}")
# else:
#     print(
#         f"Wish a happy birthday to {selected_name} who was born on {birthdays.get(selected_name)}"
#     )


# Exercise 3: Add Your Own Birthday
# Instructions
# Add this new code: before asking the user to input a person’s name to look up, ask the user to add a new birthday:
# Ask the user for a person’s name – store it in a variable.
# Ask the user for this person’s birthday (in the format “YYYY/MM/DD”) - store it in a variable.
# Now add this new data into your dictionary.
# Make sure that if the user types any name that exists in the dictionary – including the name that he entered himself – the corresponding birthday is found and displayed.

# user_name = input("Hello stranger, what is your name? ")
# user_birthday = input("and what is your birthday? (YYYY/MM/DD) ")
# birthdays[user_name] = user_birthday
# print(f"So {user_name}. You can check out the birthdays for the list members")
# selected_name = input(
#     f"Please select one of the names on the list {' '.join(list(birthdays.keys()))} "
# )
# if birthdays.get(selected_name) == None:
#     print(f"Sorry, we don’t have the birthday information for {selected_name}")
# else:
#     print(
#         f"Wish a happy birthday to {selected_name} who was born on {birthdays.get(selected_name)}"
#     )

# Exercise 4: Fruit Shop
# Instructions
# items = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
# Using the dictionary above, each key-value pair represents an item and its price - print all the items and their prices in a sentence.
# Using the dictionary below, each value are dictionaries containing both the price and the amount of items in stock -
# write some code to calculate how much it would cost to buy everything in stock.
items = {
    "banana": {"price": 4, "stock": 10},
    "apple": {"price": 2, "stock": 5},
    "orange": {"price": 1.5, "stock": 24},
    "pear": {"price": 3, "stock": 1},
}

# item_string = ""
# for k, v in items.items():
#     item_string = f"{item_string}you can buy {k}s for the price of {v}, "
# print(f"Hello customer - {item_string}")

total_cost = 0
for k, v in items.items():
    total_cost += v["price"] * v["stock"]
print(total_cost)
