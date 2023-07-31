# Reverse The Sentence
# Write a program to reverse the sentence wordwise.
# Input:
# You have entered a wrong domain
# Output:
# domain wrong a entered have You
start_string = "You have entered a wrong domain"
end_string = start_string.split(" ")
print(" ".join(end_string[::-1]))
