# Exercise
# Analyse the code below. What will be the outputs ?

# Explain the goal of the methods


# class Circle:
#     color = "red"

#     def __init__(self, diameter):
#         self.diameter = diameter

#     def grow(self, factor=2):
#         self.diameter = self.diameter * factor

#     def get_color(self):
#         return Circle.color


# circle1 = Circle(2)
# print(circle1.color)
# print(Circle.color)
# print(circle1.get_color())
# circle1.grow(3)
# print(circle1.diameter)

# Exercise
# Analyze the code below. What will be the output ?


# class MyClass(object):
#     count = 0

#     def __init__(self, val):
#         self.val = val
#         MyClass.count += 1

#     def set_val(self, newval):
#         self.val = newval

#     def get_val(self):
#         return self.val

#     @classmethod
#     def get_count(cls):
#         return cls.count


# object_1 = MyClass(10)
# print("\nValue of object : %s" % object_1.get_val())
# print(MyClass.get_count())

# object_2 = MyClass(20)
# print("\nValue of object : %s" % object_2.get_val())
# print(MyClass.get_count())


# Exercise
# Analyze the code below. What will be the output ?


# class MyClass(object):
#     count = 0

#     def __init__(self, val):
#         self.val = self.filterint(val)
#         MyClass.count += 1

#     @staticmethod
#     def filterint(value):
#         if not isinstance(value, int):
#             print("Entered value is not an INT, value set to 0")
#             return 0
#         else:
#             return value


# a = MyClass(5)
# b = MyClass(10)
# c = MyClass(15)

# print(a.val)
# print(b.val)
# print(c.val)
# print(a.filterint(100))

# Exercise
# Analyse the code below before executing it. What will be the output ?


# class PrintList(object):
#     def __init__(self, my_list):
#         self.mylist = my_list

#     def __repr__(self):
#         return str(self.mylist)


# printlist = PrintList(["a", "b", "c"])
# print(printlist.__repr__())

# Exercise
# Try to create a countdown to your birthday !

# For example : "My birthday is in 45 days, and 10:29:46"

import datetime

secs_in_a_day = 86400
secs_in_a_hour = 3600
secs_in_a_min = 60

today = datetime.datetime.now()
birth_date = datetime.datetime(2023, 12, 3)
till_birthday = birth_date - today

seconds = int(till_birthday.total_seconds())

days, seconds = divmod(seconds, secs_in_a_day)
hours, seconds = divmod(seconds, secs_in_a_hour)
minutes, seconds = divmod(seconds, secs_in_a_min)

time_fmt = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

print(f"My birthday is in {(till_birthday).days} days and {time_fmt}")
