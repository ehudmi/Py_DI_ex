# Exercise 1: Concatenate Lists
# Instructions
# Write code that concatenates two lists together without using the + sign.

first_list = ["my", "big", "fat"]
second_list = ["black", "mama's", "ass"]
first_list.extend(second_list)


# Exercise 2: Range Of Numbers
# Instructions
# Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.

for item in list(range(1500, 2501)):
    if item % 5 == 0 and item % 7 == 0:
        print(item)


# Exercise 3: Check The Index
# Instructions
# Using this variable

names = ["Samus", "Cortana", "V", "Link", "Mario", "Cortana", "Samus"]

# Ask a user for their name, if their name is in the names list print out the index of the first occurence of the name.
# Example: if input is 'Cortana' we should be printing the index 1

user_name = input("What is your name? ")
if user_name in names:
    print(names.index(user_name))

# Exercise 4: Greatest Number
# Instructions
# Ask the user for 3 numbers and print the greatest number.
#     Test Data
#     Input the 1st number: 25
#     Input the 2nd number: 78
#     Input the 3rd number: 87

#     The greatest number is: 87

number_list = list()
number_list.append(int(input("input the 1st number ")))
number_list.append(int(input("input the 2nd number ")))
number_list.append(int(input("input the 3rd number ")))
print(f"The greatest number is {sorted(number_list)[-1]}")

# Exercise 5: The Alphabet
# Instructions
# Create a string of all the letters in the alphabet
# Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant.

alphabet_string = "abcdefghijklmnopqrstuvwxyz"
for item in alphabet_string:
    if item == "a" or item == "e" or item == "i" or item == "o" or item == "u":
        print(f"Thi is the letter {item} - it is a vowel")
    else:
        print(f"Thi is the letter {item} - it is a consonant")

# Exercise 6: Words And Letters
# Instructions
# Ask a user for 7 words, store them in a list named words.
# Ask the user for a single character, store it in a variable called letter.
# Loop through the words list and print the index of the first appearence of the letter variable in each word of the list.
# If the letter doesn’t exist in one of the words, print a friendly message with the word and the letter.

words = list()
counter = 0
while counter < 7:
    words.append(input("Please enter a word "))
    counter += 1
letter = input("Please select a letter ")
for item in words:
    if letter in item:
        print(f"the letter {letter} is in index position {item.index(letter)}")
    else:
        print(f"the letter {letter} doesn't appear in the word {item}")

# Exercise 7:
# Instructions
# Create a list of numbers from one to one million and then use min() and max() to make sure your list actually starts at one and ends at one million. Use the sum() function to see how quickly Python can add a million numbers.

huge_list = list(range(1, 1000001))
print(min(huge_list))
print(max(huge_list))
print(sum(huge_list))

# Exercise 8 : List And Tuple
# Instructions
# Write a program which accepts a sequence of comma-separated numbers. Generate a list and a tuple which contain every number.
# Suppose the following input is supplied to the program: 34,67,55,33,12,98

# Then, the output should be:

# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

user_input = input("insert a series of numbers separated by commas ")
user_list = list(user_input.split(","))
user_tuple = tuple(user_input.split(","))
print(user_list)
print(user_tuple)

# Exercise 9 : Random Number
# Instructions
# Ask the user to input a number from 1 to 9 (including).
# Get a random number between 1 and 9. Hint: random module.
# If the user guesses the correct number print a message that says Winner.
# If the user guesses the wrong number print a message that says better luck next time.
# Bonus: use a loop that allows the user to keep guessing until they want to quit.
# Bonus 2: on exiting the loop tally up and display total games won and lost.

from random import randint

user_guess = ""
count_won = 0
count_lost = 0
while user_guess != "quit":
    comp_number = randint(1, 9)
    user_guess = input("Guess a number between 1 and 9 ")
    if user_guess == "quit":
        break
    if int(user_guess) == comp_number:
        print("Winner")
        count_won += 1
    else:
        print("better luck next time")
        count_lost += 1
print(f"You have won {count_won} games and lost {count_lost} games")
