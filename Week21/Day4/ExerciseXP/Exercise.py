# 🌟 Exercise 1 – Random Sentence Generator
# Instructions
# Description: In this exercise we will create a random sentence generator. We will do this by asking the user how long
# the sentence should be and then printing the generated sentence.

# Hint : The generated sentences do not have to make sense.

# Download this word list
# http://norvig.com/ngrams/sowpods.txt

# Save it in your development directory.

# Create a function called get_words_from_file. This function should read the file’s content and return the words as a
# collection. What is the correct data type to store the words?
from random import randint

word_list = []


def get_words_from_file():
    with open("./words.txt") as words:
        for line in words:
            word_list.append(line[:-1].lower())
    return word_list


def get_random_sentence(num):
    sentence = ""
    for n in range(0, num):
        select_word = word_list[randint(0, len(word_list))]
        sentence = sentence + " " + select_word
    print(sentence)


def main():
    get_words_from_file()
    print(
        "This is a simple program creating a random sentence base on the number of words you select"
    )

    while True:
        try:
            user_input = int(
                input("How many words would you like in your sentence? 2 to 20  ")
            )
            if 1 < user_input < 21:
                get_random_sentence(user_input)
            else:
                print("Please make sure the number is between 2 and 20")
        except ValueError:
            print("you did not input a number")
            return False


main()

# Create another function called get_random_sentence which takes a single parameter called length. The length parameter
# will be used to determine how many words the sentence should have. The function should:
# use the words list to get your random words.
# the amount of words should be the value of the length parameter.

# Take the random words and create a sentence (using a python method), the sentence should be lower case.

# Create a function called main which will:

# Print a message explaining what the program does.

# Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your
# data and test your validation!
# If the user inputs incorrect data, print an error message and end the program.
# If the user inputs correct data, run your code.


# 🌟 Exercise 2: Working With JSON
# Instructions
import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

json_dict = json.loads(sampleJson)
print(json_dict["company"]["employee"]["payable"]["salary"])
json_dict["company"]["employee"].update({"birth_date": "03/12/1966"})
print(json_dict)

# Access the nested “salary” key from the JSON-string above.
# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
# Save the dictionary as JSON to a file.

with open("json_file", "w") as j_file:
    json.dump(json_dict, j_file, indent=2, sort_keys=True)
