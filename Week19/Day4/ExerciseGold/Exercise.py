# Exercise 1 : What’s Your Name ?
# Instructions
# Write a function called get_full_name() that takes three arguments: 1: first_name, 2: middle_name 3: last_name.
# middle_name should be optional, if it’s omitted by the user, the name returned should only contain the first and
# the last name.
# For example, get_full_name(first_name="john", middle_name="hooker", last_name="lee") will return John Hooker Lee.
# But get_full_name(first_name="bruce", last_name="lee") will return Bruce Lee.


def get_full_name(first_name, last_name, middle_name=""):
    print(f"{first_name} {middle_name} {last_name}")


get_full_name(first_name="john", middle_name="hooker", last_name="lee")
get_full_name(first_name="bruce", last_name="lee")

# Exercise 2 : From English To Morse
# Instructions
# Write a function that converts English text to morse code and another one that does the opposite.
# Hint: Check the internet for a translation table, every letter is separated with a space and every word is
# separated with a slash /.

CHARS_TO_MORSE_CODE_MAPPING = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
}


def morse_english_map(select_dict):
    reverse_dict = {}
    for k, v in select_dict.items():
        reverse_dict[v] = k
    return reverse_dict


MORSE_TO_CHARS_MAPPING = morse_english_map(CHARS_TO_MORSE_CODE_MAPPING)


def english_morse(user_string):
    result = []
    for i in range(0, len(user_string)):
        if user_string[i] == " ":
            result.append("/")
        else:
            result.append(f"{CHARS_TO_MORSE_CODE_MAPPING.get(user_string[i])} ")
    print("".join(result))


def morse_english(user_string):
    result = []
    morse_string_list = user_string.split(" ")
    # print(morse_string_list)
    for i in range(0, len(morse_string_list)):
        if morse_string_list[i][0] == "/":
            result.append(" ")
            result.append(MORSE_TO_CHARS_MAPPING.get(morse_string_list[i][1:]))
        else:
            result.append(MORSE_TO_CHARS_MAPPING.get(morse_string_list[i]))
    print("".join(result).capitalize())


def select_dict(dict_type, user_input):
    if dict_type == "morse":
        english_morse(user_input.upper())
    else:
        morse_english(user_input)


select_dict(
    input("Would you like to translate to English or to Morse? "),
    input("Please enter the text to translate "),
)
