# Count Occurence
# Write a program which takes a string and a character as an input, and finds out the number of occurrences the
# character has in the string.

# String: Programming is cool!
# Character: o
# 3


# String: This is a great example
# Character: y
# 0


def count_occur(user_string, char):
    print(user_string.count(char))


count_occur("Programming is cool!", "o")
count_occur("This is a great example", "y")
