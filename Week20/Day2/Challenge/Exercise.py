# Instructions : Old MacDonald’s Farm
# Take a look at the following code and output:
# File: market.py

# macdonald = Farm("McDonald")
# macdonald.add_animal('cow',5)
# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)
# print(macdonald.get_info())
# Output

# McDonald's farm

# cow : 5
# sheep : 2
# goat : 12

#     E-I-E-I-0!


# Create the code that is needed to receive the result provided above. Below are a few questions to assist you
# with your code:

# Create a class called Farm. How should it be implemented?
# Does the Farm class need an __init__ method? If so, what parameters should it take?
# How many methods does the Farm class need?
# Do you notice anything interesting about the way we are calling the add_animal method? What parameters should
# this function have? How many…?
# Test your code and make sure you get the same results as the example above.
# Bonus: nicely line the text in columns as seen in the example above. Use string formatting.


class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, name, quantity=1):
        if name in self.animals.keys():
            self.animals.update({name: quantity + 1})
        else:
            self.animals.update({name: quantity})

    def get_info(self):
        output_string = f"{self.name}'s farm\n\n"
        for k, v in self.animals.items():
            output_string = output_string + f"{k}:{v}\n"
        return output_string + "\n\tE-I-E-I-0!"

    def get_animals_type(self):
        self.animals_sorted = sorted(self.animals)

    def get_short_info(self):
        self.get_animals_type()
        output_string = f"{self.name}'s farm has"
        for item in self.animals_sorted:
            if item == self.animals_sorted[-1]:
                output_string = f"{output_string} and {item}"
            else:
                output_string = f"{output_string} {item}s,"
        return output_string


macdonald = Farm("McDonald")
macdonald.add_animal("cow", 5)
macdonald.add_animal("sheep")
macdonald.add_animal("sheep")
macdonald.add_animal("goat", 12)
print(macdonald.get_info())


# Expand The Farm
# Add a method called get_animal_types to the Farm class. This method should return a sorted list of all the animal
# types (names) in the farm. With the example above, the list should be: ['cow', 'goat', 'sheep'].

# Add another method to the Farm class called get_short_info. This method should return the following
# string: “McDonald’s farm has cows, goats and sheep.”. The method should call the get_animal_types function to
# get a list of the animals.
