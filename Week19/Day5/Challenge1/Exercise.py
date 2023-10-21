# Exercise 1
# Instructions
# Write a script that inserts an item at a defined index in a list.

test_list = [1, 2, 3, 4, 5]


def insert_item(item, index):
    test_list.insert(index, item)
    print(test_list)


insert_item(7, 10)


# Exercise 2
# Instructions
# Write a script that counts the number of spaces in a string.


def count_spaces(user_string):
    print(user_string.count(" "))


count_spaces(input("Please enter a string "))

# Exercise 3
# Instructions
# Write a script that calculates the number of upper case letters and lower case letters in a string.


def count_case(user_string):
    upper_case = 0
    lower_case = 0
    for char in user_string:
        if 65 <= ord(char) <= 90:
            upper_case += 1
        elif 97 <= ord(char) <= 122:
            lower_case += 1
    print(
        f"There are {upper_case} upper case characters and {lower_case} lower case characters in the string you wrote"
    )


count_case(input("Please give me a string "))

# Exercise 4
# Instructions
# Write a function to find the sum of an array without using the built in function:

#     >>>my_sum([1,5,4,2])
#     >>>12


def my_sum(user_list):
    sum_calc = 0
    for item in user_list:
        sum_calc += item
    print(sum_calc)


my_sum([1, 5, 4, 2])

# Exercise 5
# Instructions
# Write a function to find the max number in a list

#     >>>find_max([0,1,3,50])
#     >>>50


def find_max(num_list):
    max_num = num_list[0]
    for item in num_list:
        if item > max_num:
            max_num = item
    print(max_num)


find_max([0, 1, 3, 50])


# Exercise 6
# Instructions
# Write a function that returns factorial of a number

#     >>>factorial(4)
#     >>>24


def factorial(user_num):
    factor = 1
    for num in range(user_num, 1, -1):
        factor = factor * num
    print(factor)


factorial(4)


# Exercise 7
# Instructions
# Write a function that counts an element in a list (without using the count method):

#     >>>list_count(['a','a','t','o'],'a')
#     >>>2


def list_count(user_list_1, char):
    counter = 0
    for item in user_list_1:
        if item == char:
            counter += 1
    print(counter)


list_count(["a", "a", "t", "o"], "a")


# Exercise 8
# Instructions
# Write a function that returns the L2-norm (square root of the sum of squares) of the sum of a list:

#     >>>norm([1,2,2])
#     >>>3
from math import sqrt


def norm(user_list_2):
    sqr_list = [item**2 for item in user_list_2]
    sqr_root = sqrt(sum(sqr_list))
    print(sqr_root)


norm([1, 2, 2])

# Exercise 9
# Instructions
# Write a function to find if an array is monotonic (sorted either ascending of descending)

#     >>>is_mono([7,6,5,5,2,0])
#     >>>True

#     >>>is_mono([2,3,3,3])
#     >>>True

#     >>>is_mono([1,2,0,4])
#     >>>False


def is_mono(user_list_3):
    user_list_sorted = sorted(user_list_3)
    user_list_reverse = sorted(user_list_3, reverse=True)
    if user_list_3 == user_list_sorted:
        print(True)
    elif user_list_3 == user_list_reverse:
        print(True)
    else:
        print(False)


is_mono([7, 6, 5, 5, 2, 0])


# Exercise 10
# Instructions
# Write a function that prints the longest word in a list.


def longest_word(user_list_4):
    word = ""
    for item in user_list_4:
        if len(item) > len(word):
            word = item
    print(word)


longest_word(["I", "love", "your", "dress"])


# Exercise 11
# Instructions
# Given a list of integers and strings, put all the integers in one list, and all the strings in another one.


def split_int_string(user_list_5):
    int_list = []
    string_list = []
    for item in user_list_5:
        try:
            int(item)
            int_list.append(item)
        except ValueError:
            string_list.append(item)
    print(int_list)
    print(string_list)


split_int_string([3, "my", "bunny", "is", 8, 9])

# Exercise 12
# Instructions
# Write a function to check if a string is a palindrome:

#     >>>is_palindrome('radar')
#     >>>True

#     >>>is_palindrome('John)
#     >>>False


def is_palindrome(user_string_1):
    user_list = list(user_string_1)
    user_list_reverse = user_list[::-1]
    if user_list == user_list_reverse:
        print(True)
    else:
        print(False)


is_palindrome("John")

# Exercise 13
# Instructions
# Write a function that returns the amount of words in a sentence with length > k:

#     >>>sentence = 'Do or do not there is no try'
#     >>>k=2
#     >>>sum_over_k(sentence,k)
#     >>>3

sentence = "Do or do not there is no try"
k = 2


def sum_over_k(sentence, k):
    sentence_list = sentence.split(" ")
    long_counter = 0
    for item in sentence_list:
        if len(item) > k:
            long_counter += 1
    print(long_counter)


sum_over_k(sentence, k)

# Exercise 14
# Instructions
# Write a function that returns the average value in a dictionary (assume the values are numeric):

#     >>>dict_avg({'a': 1,'b':2,'c':8,'d': 1})
#     >>>3


def dict_avg(user_dict):
    sum_values = 0
    for v in user_dict.values():
        sum_values += v
    print(sum_values / len(user_dict))


dict_avg({"a": 1, "b": 2, "c": 8, "d": 1})


# Exercise 15
# Instructions
# Write a function that returns common divisors of 2 numbers:

#     >>>common_div(10,20)
#     >>>[2,5,10]


# Exercise 16
# Instructions
# Write a function that test if a number is prime:

#     >>>is_prime(11)
#     >>>True


# Exercise 17
# Instructions
# Write a function that prints elements of a list if the index and the value are even:

#     >>>weird_print([1,2,2,3,4,5])
#     >>>[2,4]


# Exercise 18
# Instructions
# Write a function that accepts an undefined number of keyworded arguments and return the count of different types:

#     >>>type_count(a=1,b='string',c=1.0,d=True,e=False)
#     >>>int: 1, str:1 , float:1, bool:2


# Exercise 19
# Instructions
# Write a function that mimics the builtin .split() method for strings.
# By default the function uses whitespace but it should be able to take an argument for any character and
# split with that argument.


# Exercise 20
# Instructions
# Convert a string into password format.
# Example:
# input : "mypassword"
# output: "***********"
