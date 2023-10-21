# Exercise 1
print("Hello World\n" * 4 + "I love PYTHON\n" * 4)

# Exercise 2
user_month = input("Select a month - (1 to 12) ")
if 3 <= int(user_month) <= 5:
    print("You selected spring")
elif 6 <= int(user_month) <= 8:
    print("You selected summer")
elif 9 <= int(user_month) <= 11:
    print("You selected autumn")
else:
    print("You selected winter")
