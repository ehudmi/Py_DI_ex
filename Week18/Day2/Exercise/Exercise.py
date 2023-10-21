# Exercise 1
print("Hello World\n" * 4)

# Exercise 2
print((99**3) * 8)

# Exercise 3
# 5 < 3 -               False
# 3 == 3 -              True
# 3 == "3" -            False
# "3" > 3 -             Type Error
# "Hello" == "hello" -  False

# Exercise 4

computer_brand = "Asus"
print(f"I have an {computer_brand} computer")

# Exercise 5

name = "Ehud Miron"
age = 56
shoe_size = 46
info = f"my name is {name} and I am {age} years old and my shoe size is {shoe_size}"
print(info)

# Exercise 6

a = 7
b = 3

if a > b:
    print("Hello World")

# Exercise 7

user_number = input("choose a number between 0 and 100 ")
if int(user_number) % 2 == 0:
    print("Your number is an even number")
else:
    print("your number is an odd number")

# Exercise 8

user_name = input("What is your name? ")
my_name = "Ehud"

if user_name == my_name:
    print("Are you my clone?")
else:
    print("What an original name you have")

# Exercise 9

user_height = input("What is your height in centimeters? ")
if int(user_height) > 145:
    print("You are tall enough to ride ")
else:
    print("You need to grow some more to ride")
