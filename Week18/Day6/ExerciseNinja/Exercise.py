# Exercise 1 : Cars
# Instructions
# Copy the following string into your code: "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet".
cars_string = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"

# Convert it into a list using Python (don’t do it by hand!).

cars_list = cars_string.split(",")
# print(cars_list)

# Print out a message saying how many manufacturers/companies are in the list.

# print(f"there are {len(cars_list)} manufacturers on the list")

# Print the list of manufacturers in reverse/descending order (Z-A).

# print(sorted(cars_list, reverse=True))

# Using loops or list comprehension:
# Find out how many manufacturers’ names have the letter ‘o’ in them.

# cars_list_1 = [name for name in cars_list if name.find("o") >= 0]
# print(cars_list_1)

# Find out how many manufacturers’ names do not have the letter ‘i’ in them.

# cars_list_1 = [name for name in cars_list if name.find("i") < 0]
# print(cars_list_1)

# Bonus: There are a few duplicates in this list:["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
# Remove these programmatically. (Hint: you can use set to help you).
# Print out the companies without duplicates, in a comma-separated string with no line-breaks (eg. “Acura, Alfa Romeo, Aston Martin, …”), also print out a message saying how many companies are now in the list.

new_cars_list = [
    "Honda",
    "Volkswagen",
    "Toyota",
    "Ford Motor",
    "Honda",
    "Chevrolet",
    "Toyota",
]

# print(f"{', '.join(set(new_cars_list))}")
# print(f"there are now {len(set(new_cars_list))} manufacturers on the list")

# Bonus: Print out the list of manufacturers in ascending order (A-Z), but reverse the letters of each manufacturer’s name.

new_cars_list_2 = sorted(set(new_cars_list))
new_cars_list_reverse = []
for item in new_cars_list_2:
    item = item[::-1]
    new_cars_list_reverse.append(item)
    print(item)

print(f"{', '.join(new_cars_list_reverse)}")
