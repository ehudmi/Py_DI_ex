# Exercise 3

#  3 <= 3 < 9                           True
#  3 == 3 == 3                          True
#  bool(0)                              False
#  bool(5 == "5")                       False
#  bool(4 == 4) == bool("4" == "4")     True
#  bool(bool(None))                     False
x = 1 == True
y = 1 == False
a = True + 4
b = False + 10

print("x is", x)  # True
print("y is", y)  # False
print("a:", a)  # 5
print("b:", b)  # 10

# Exercise 4
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print(len(my_text))

# Exercise 5
user_string = input("Write the longest possible text without the character A ")
max_characters = 0
if len(user_string) > max_characters:
    max_characters = len(user_string)
    print(f"The record number of characters so far is {max_characters}")
else:
    print(f"you haven't beaten the record - {max_characters}")
