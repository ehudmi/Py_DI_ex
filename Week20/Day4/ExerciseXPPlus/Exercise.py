# Exercise 1 : Family
# Instructions
# Create a class called Family and implement the following attributes:

# members: list of dictionaries with the following keys : name, age, gender and is_child (boolean).
# last_name : (string)
# Initial members data:

# initial_data_1 = [
#     {"name": "Michael", "age": 35, "gender": "Male", "is_child": False},
#     {"name": "Sarah", "age": 32, "gender": "Female", "is_child": False},
# ]


# 2. Implement the following methods:

# born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
# is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
# family_presentation: a method that prints the family’s last name and all the members’ first name.


class Family:
    def __init__(self, last_name):
        self.members = [
            {"name": "Michael", "age": 35, "gender": "Male", "is_child": False},
            {"name": "Sarah", "age": 32, "gender": "Female", "is_child": False},
        ]
        self.last_name = last_name

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"congrats - {self.members[-1]['name']} was born")

    def is_18(self, name):
        self._adult = 0
        for item in self.members:
            if item["name"] == name and item["age"] >= 18:
                self._adult = self.members.index(item)
                return True
            elif item["name"] == name and item["age"] < 18:
                return False

    def family_presentation(self):
        print(f"{self.last_name} {', '.join([item['name'] for item in self.members])}")


# cohen_fam = Family("Cohen")
# cohen_fam.born(name="Suzie", gender="Female", is_child=True, age=0)
# print(cohen_fam.is_18("Suzie"))
# print(cohen_fam.is_18("Micahel"))
# print(cohen_fam.is_18("Michael"))
# print(cohen_fam.is_18("Sarah"))

# cohen_fam.family_presentation()

# Exercise 2 : TheIncredibles Family
# Instructions
# Create a class called TheIncredibles. This class should inherit from the Family class:
# This is no random family they are an incredible family, therefore we need to add the following keys to
# our dictionaries: power and incredible_name.

# Initial members data:

# initial_data_2 = [
#     {
#         "name": "Michael",
#         "age": 35,
#         "gender": "Male",
#         "is_child": False,
#         "power": "fly",
#         "incredible_name": "MikeFly",
#     },
#     {
#         "name": "Sarah",
#         "age": 32,
#         "gender": "Female",
#         "is_child": False,
#         "power": "read minds",
#         "incredible_name": "SuperWoman",
#     },
# ]


# Add a method called use_power, this method should print the power of a member only if they are over 18 years old.
# If not raise an exception (look up exceptions) which stated they are not over 18 years old.


# Add a method called incredible_presentation which :

# Prints the family’s last name and all the members’ first name (ie. use the super() function, to call the
# family_presentation method)
# Prints all the members’ incredible name and power.

# Call the incredible_presentation method.


# Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.


# Call the incredible_presentation method again.


class TheIncredibles(Family):
    def __init__(self, last_name):
        super().__init__(last_name)
        self.members = [
            {
                "name": "Michael",
                "age": 35,
                "gender": "Male",
                "is_child": False,
                "power": "fly",
                "incredible_name": "MikeFly",
            },
            {
                "name": "Sarah",
                "age": 32,
                "gender": "Female",
                "is_child": False,
                "power": "read minds",
                "incredible_name": "SuperWoman",
            },
        ]

    def use_power(self, name):
        if self.is_18(name) == True:
            print(
                f"{self.members[self._adult]['name']} has {self.members[self._adult]['power']}"
            )
        else:
            raise Exception(f"{name} is not over 18")

    def incredible_presentation(self):
        self.family_presentation()
        for item in self.members:
            self.use_power(item["name"])


incredible = TheIncredibles("Parr")
incredible.incredible_presentation()

incredible.born(name="Jack", gender="Male", age=0, is_child=True, power="Unknown Power")
incredible.incredible_presentation()
incredible.use_power("Sarah")
