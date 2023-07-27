# Challenge 1
# Ask the user for a number and a length.
# Create a program that prints a list of multiples of the number until the list length reaches length.
# Examples

# number: 7 - length 5 ➞ [7, 14, 21, 28, 35]

# number: 12 - length 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

# number: 17 - length 6 ➞ [17, 34, 51, 68, 85, 102]

user_number = int(input("Please choose a number "))
user_length = int(input("Please select a length "))
counter = 1
number_list = list()
while counter < user_length + 1:
    number_list.append(user_number * counter)
    counter += 1
print(f"number: {user_number} - length {user_length} -> {number_list}")

# Challenge 2
# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
# Examples

# user's word : "ppoeemm" ➞ "poem"

# user's word : "wiiiinnnnd" ➞ "wind"

# user's word : "ttiiitllleeee" ➞ "title"

# user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"
# Notes
# Final strings won’t include words with double letters (e.g. “passing”, “lottery”).

user_list = list(input("Please enter a string "))
for item in user_list:
    if user_list.count(item) > 1:
        user_list.remove(item)
print("".join(user_list))
