# Perfect Number
# A perfect number is a positive integer that is equal to the sum of its divisors.
# However, the number itself is not included in the sum.

# Ask the user for a number and print whether or not it is a perfect number. If yes, print True else False.
# Hint: Google perfect numbers
# Example

# Input -- Enter the number:6
# Output -- True

# Input -- Enter the number:10
# Output --  False
user_number = int(input("Enter the number "))
counter = 1
divisor_list = []
total_divisor = 0
while counter < user_number:
    if user_number % counter == 0:
        divisor_list.append(counter)
        counter += 1
    else:
        counter += 1
for item in divisor_list:
    total_divisor += item
if total_divisor == user_number:
    print("True")
else:
    print("False")
