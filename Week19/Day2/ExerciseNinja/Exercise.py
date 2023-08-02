# Exercise 1 : Box Of Stars
# Instructions
# Write a function named box_printer that takes any amount of strings (not in a list) and prints them, one per line, in a rectangular frame.
# For example calling box_printer("Hello", "World", "in", "reallylongword", "a", "frame") will result as:
# ******************
# * Hello          *
# * World          *
# * in             *
# * reallylongword *
# * a              *
# * frame          *
# ******************


# def box_printer(*user_string):
#     user_string_list = list(user_string)
#     user_string_length = set(len(item) for item in user_string_list)
#     max_length = max(user_string_length)
#     #     print(f"""
#     #     {'*'*(max_length+2)}
#     #     {for item in user_string_list:
#     # }
#     # """)
#     print("*" * (max_length + 4))
#     for item in user_string_list:
#         print("* " + item + " " * (max_length + 2 - len(item) - 1) + "*")
#     print("*" * (max_length + 4))


# box_printer("Hello", "World", "in", "reallylongword", "a", "frame")


# Exercise 2
# Analyse this code before executing it. What is the purpose of this code?
def insertion_sort(alist):
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = currentvalue


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(alist)
print(alist)
