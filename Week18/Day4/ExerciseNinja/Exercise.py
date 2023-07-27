# Exercise 1: Formula
# Instructions
# Write a program that calculates and prints a value according to this given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50.
# H is 30.
# Ask the user for a comma-separated string of numbers, use each number from the user as D in the formula and return all the results
# For example, if the user inputs: 100,150,180
# The output should be:

# 18,22,24

from math import sqrt

user_list = input("Please enter list of numbers separated by commas ").split(",")
result_list = list()
for item in user_list:
    result_list.append(int(sqrt((2 * 50 * int(item)) / 30)))
print(result_list)

# Exercise 2 : List Of Integers
# Instructions
# Given a list of 10 integers to analyze. For example:

#     [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]
#     [44, 91, 8, 24, -6, 0, 56, 8, 100, 2]
#     [3, 21, 76, 53, 9, -82, -3, 49, 1, 76]
#     [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]
# Store the list of numbers in a variable.
# Print the following information:
# a. The list of numbers – printed in a single line
# b. The list of numbers – sorted in descending order (largest to smallest)
# c. The sum of all the numbers
# A list containing the first and the last numbers.
# A list of all the numbers greater than 50.
# A list of all the numbers smaller than 10.
# A list of all the numbers squared – eg. for [1, 2, 3] you would print “1 4 9”.
# The numbers without any duplicates – also print how many numbers are in the new list.
# The average of all the numbers.
# The largest number.
# 10.The smallest number.
# 11.Bonus: Find the sum, average, largest and smallest number without using built in functions.
# 12.Bonus: Instead of using pre-defined lists of numbers, ask the user for 10 numbers between -100 and 100. Ask the user for an integer between -100 and 100 – repeat this question 10 times. Each number should be added into a variable that you created earlier.
# 13.Bonus: Instead of asking the user for 10 integers, generate 10 random integers yourself. Make sure that these random integers are between -100 and 100.
# 14.Bonus: Instead of always generating 10 integers, let the amount of integers also be random! Generate a random positive integer no smaller than 50.
# 15.Bonus: Will the code work when the number of random numbers is not equal to 10?

from random import randint

counter = 0
user_list = list()
random_items = randint(50, 100)
while counter < random_items:
    # while counter < 10:
    # user_list.append(int(input("Please select an integer between -100 and 100 ")))
    user_list.append(randint(-100, 100))
    counter += 1
print(f"this is the list: {user_list}")
sorted_list = user_list.copy()
sorted_list.sort(reverse=True)
print(f"this is the reverse sorted list: {sorted_list}")
print(f"this is the first number {user_list[0]}, and this is the last {user_list[-1]}")
big_num_list = list()
small_num_list = list()
square_list = list()
sum_list = 0
for item in user_list:
    square_list.append(item**2)
    sum_list += item
    if item < 10:
        small_num_list.append(item)
    if item > 50:
        big_num_list.append(item)
print(f"these are the numbers larger than 50: {big_num_list}")
print(f"these are the numbers smaller than 10: {small_num_list}")
print(f"this is the list with all numbers squared: {square_list}")
user_set = set(user_list)
print(f"this is the set based upon the list: {user_set}")
print(f"there are {len(user_set)} items in the set")
print(f"this is the sum of all items in the list: {sum_list}")
print(f"this is the average: {sum_list / len(user_list)}")
print(f"this is the smallest number: {sorted(user_list)[0]}")
print(f"this is the largest number: {sorted(user_list)[-1]}")


# Exercise 3: Working On A Paragraph
# Find an interesting paragraph of text online. (Please keep it appropriate to the social context of our class.)
# Paste it to your code, and store it in a variable.
# Let’s analyze the paragraph. Print out a nicely formatted message saying:
# How many characters it contains (this one is easy…).
# How many sentences it contains.
# How many words it contains.
# How many unique words it contains.
# Bonus: How many non-whitespace characters it contains.
# Bonus: The average amount of words per sentence in the paragraph.
# Bonus: the amount of non-unique words in the paragraph.

my_paragraph = "During the late-sixth and early-fifth centuries BCE, this term found its way into ancient Greek, where it was used with negative connotations to apply to rites that were regarded as fraudulent, unconventional, and dangerous.[14] The Latin language adopted this meaning of the term in the first century BCE. Via Latin, the concept became incorporated into Christian theology during the first century CE. Early Christians associated magic with demons, and thus regarded it as against Christian religion. This concept remained pervasive throughout the Middle Ages, when Christian authors categorised a diverse range of practices—such as enchantment, witchcraft, incantations, divination, necromancy, and astrology—under the label 'magic'. In early modern Europe, Protestants often claimed that Roman Catholicism was magic rather than religion, and as Christian Europeans began colonizing other parts of the world in the sixteenth century, they labelled the non-Christian beliefs they encountered as magical. In that same period, Italian humanists reinterpreted the term in a positive sense to express the idea of natural magic. Both negative and positive understandings of the term recurred in Western culture over the following centuries."
print(f"the paragraph contains {len(my_paragraph)} characters")
print(f"the paragraph contains {my_paragraph.count('.')} sentences")
print(f"the paragraph contains {my_paragraph.count(' ')} words")
words_list = my_paragraph.split(" ")
words_set = set(words_list)
print(f"the paragraph contains {len(words_set)} unique words")
print(
    f"the paragraph contains {len(my_paragraph)-my_paragraph.count(' ')} non-whitespace characters"
)
print(
    f"the paragraph contains an average of {my_paragraph.count(' ')/my_paragraph.count('.')} words per sentence"
)
print(
    f"the paragraph contains {my_paragraph.count(' ')-len(words_set)} non-unique words"
)

# Exercise 4
# Instructions
# Write a program that prints the frequency of the words from the input.

# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

# Then, the output should be:

#     2:2
#     3.:1
#     3?:1
#     New:1
#     Python:5
#     Read:1
#     and:1
#     between:1
#     choosing:1
#     or:2
#     to:1

input_list = (input("Gimme your words ")).split(" ")
input_set = set(input_list)
for item in input_set:
    print(f"{item} : {input_list.count(item)}")
