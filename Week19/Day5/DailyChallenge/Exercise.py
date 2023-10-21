# Challenge 1 : Sorting
# Instructions
# Write a program that accepts a comma separated sequence of words as input and prints the words in a
# comma-separated sequence after sorting them alphabetically.
# Use List Comprehension
# Example:


def string_order(user_string):
    print(",".join(sorted(user_string.split(","))))


string_order("without,hello,bag,world")

# Suppose the following input is supplied to the program: without,hello,bag,world
# Then, the output should be: bag,hello,without,world


# Challenge 2 : Longest Word
# Instructions
# Write a function that finds the longest word in a sentence. If two or more words are found,
# return the first longest word.
# Characters such as apostrophe, comma, period count as part of the word (e.g. O’Connor is 8 characters long).
# Examples

# longest_word("Margaret's toy is a pretty doll.") ➞ "Margaret's"

# longest_word("A thing of beauty is a joy forever.") ➞ "forever."

# longest_word("Forgetfulness is by all means powerless!") ➞ "Forgetfulness"


def longest_word(user_string_1):
    longest = ""
    user_list_1 = user_string_1.split(" ")
    for item in user_list_1:
        if len(item) > len(longest):
            longest = item
    print(longest)


longest_word("A thing of beauty is a joy forever.")
