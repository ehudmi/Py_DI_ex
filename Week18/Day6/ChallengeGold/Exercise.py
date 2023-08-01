# Instructions
# In cryptography, a Caesar cipher is one of the simplest and most widely known encryption techniques.
# It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

# For example, with a left shift of 3 –> D would be replaced by A,
# –> E would become B, and so on.

# The method is named after Julius Caesar, who used it in his private correspondence.

# Create a python program that encrypts and decrypts messages with caesar cipher.
# The user enters the program, and then the program asks him if he wants to encrypt or decrypt, and then execute encryption/decryption on a given message and a given shift.

# Check out this tutorial

# Hint:

# for letter in text:
#     cipher_text += chr(ord(letter) + 3)
alphabet_string = "abcdefghijklmnopqrstuvwxyz"
alphabet_list = [char for char in alphabet_string]
conv_type = input("would you like to decrypt or encrypt? ")
shift_size = int(input("What is the shift size? "))
user_string = input("Please type the message for action ")
solution_string = ""
if conv_type == "encrypt":
    for item in user_string:
        if item in alphabet_list:
            index = alphabet_list.index(item)
            if index + shift_size < len(alphabet_list) - 1:
                item = alphabet_list[index + shift_size]
            else:
                item = alphabet_list[(index + shift_size) - len(alphabet_list)]
            solution_string = solution_string + item
        else:
            solution_string = solution_string.strip() + " "
    print(solution_string)
if conv_type == "decrypt":
    for item in user_string:
        if item in alphabet_list:
            index = alphabet_list.index(item)
            if index - shift_size >= 0:
                item = alphabet_list[index - shift_size]
            else:
                item = alphabet_list[(index - shift_size)]
            solution_string = solution_string + item
        else:
            solution_string = solution_string.strip() + " "
    print(solution_string)
