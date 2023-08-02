# Instructions
# Here is a python code that generate a list of 20000 random numbers, called list_of_numbers.
# Extend this code to guess how many couples of numbers in list_of_numbers sum to target_number.

import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number = 3728


def find_pair(new_number, num_list):
    for item in num_list:
        if item == new_number:
            return item


def find_couples(number):
    count_couples = 0
    couples_list = []
    for item in list_of_numbers:
        if item <= number:
            num_pair = number - item
            find_pair(num_pair, list_of_numbers)
            couples_list.append((item, num_pair))
            count_couples += 1
    print(couples_list)
    print(count_couples)


find_couples(target_number)
