# Instructions
# Write a function to compute 5/0 and use try/except to catch the exceptions.
# Bonus : use some Built-in exceptions of Python : Look here
# https://www.programiz.com/python-programming/exceptions


def div_by0(num):
    try:
        return num / 0
    except ZeroDivisionError:
        print("You can't divide a number by 0")


div_by0(5)
