# Exercise 1 : Geometry
# Instructions
# Write a class called Circle that receives a radius as an argument (default is 1.0).
# Write two instance methods to compute perimeter and area.
# Write a method that prints the geometrical definition of a circle.


class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def comp_perimeter(self):
        print(f"The perimeter of the circle is {2*3.14*self.radius}")

    def comp_area(self):
        print(f"The area of the circle is {3.14*self.radius**2}")

    def definition(self):
        print(
            """A circle is a plane figure bounded by one curved line, and such that all straight 
              lines drawn from a certain point within it to the bounding line, are equal. 
              The bounding line is called its circumference and the point, its centre"""
        )


# Exercise 2 : Custom List Class
# Instructions
# Create a class called MyList, the class should receive a list of letters.
# Add a method that returns the reversed list.
# Add a method that returns the sorted list.
# Bonus : Create a method that generates a second list with the same length as mylist. The list
# should be constructed with random numbers. (use list comprehension).

from random import randint


class MyList:
    def __init__(self, letter_list):
        self.letter_list = letter_list

    def reverse_list(self):
        return self.letter_list[::-1]

    def sorted_list(self):
        return sorted(self.letter_list)

    def num_list(self):
        return [randint(0, 10) in range(0, len(self.letter_list))]


# Exercise 3 : Restaurant Menu Manager
# Instructions
# The purpose of this exercise is to create a restaurant menu. The code will allow a manager to add and delete dishes.

# Create a python file called menu_manager.py.

# Create a class called MenuManager.

# Create a method __init__ that instantiates an attribute called menu. The menu attributes value will be all the
# current dishes (list of dictionaries). Each dish will be stored in a dictionary where the keys are name, price,
# spice level and gluten index (which value is a boolean).

# Here is a list of the dishes currently on the menu:

#     Soup – 10 – B - False
#     Hamburger – 15 - A - True
#     Salad – 18 - A - False
#     French Fries – 5 - C - False
#     Beef bourguignon– 25 - B - True

#     Meaning: For the spice level:
#        • A = not spicy,
#        • B = a little spicy,
#        • C = very spicy


# The dishes provided above should be the value of the menu attribute.

# Create a method called add_item(name, price, spice, gluten). This method will add new dishes to the menu.

# Create a method called update_item(name, price, spice, gluten). This method checks whether a dish is in the menu,
# if the dish exists then update it. If not notify the manager that the dish is not in the menu.

# Create a method called remove_item(name). This method should check if the dish is in the menu, if the dish exists
# then delete it and print the updated dictionary. If not notify the manager that the dish is not in the menu.


class MenuManager:
    def __init__(self):
        self.menu = []

    def add_item(self, name, price, spice, gluten):
        self.menu.append(
            {"name": name, "price": price, "spice": spice, "gluten": gluten}
        )

    def update_item(self, name, price, spice, gluten):
        found_flag = False
        for item in self.menu:
            if item["name"] == name:
                item["price"] = price
                item["spice"] = spice
                item["gluten"] = gluten
                found_flag = True
        if found_flag == False:
            print(f"the dish {name} is not in the menu")

    def remove_item(self, name):
        found_flag = False
        while found_flag == False:
            for item in self.menu:
                if item["name"] == name:
                    self.menu.remove(item)
                    found_flag = True
                    print(self.menu)
        if found_flag == False:
            print(f"the dish {name} is not in the menu")


restaurant = MenuManager()
restaurant.add_item("Soup", 10, "B", False)
restaurant.add_item("Hamburger", 15, "A", True)
restaurant.add_item("Salad", 18, "A", False)
restaurant.add_item("French Fries", 5, "C", False)
restaurant.add_item("Beef bourguignon", 25, "B", True)
