# Instructions :
# The goal of the exercise is to create a class that will help you analyze a specific text. A text can be just a simple
# string, like “Today, is a happy day” or it can be an external text file.


# Part I
# First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”

# Create a class called Text that takes a string as an argument and store the text in a attribute.
# Hint: You need to manually copy-paste the text, straight into the code

# Implement the following methods:
# a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a
# meaningful message.
# a method that returns the most common word in the text.
# a method that returns a list of all the unique words in the text.


# Part II
# Then, we will analyze a text coming from an external text file. Download the_stranger.txt file.
# https://github.com/devtlv/theStranger_text_W5D4PY

# Implement a classmethod that returns a Text instance but with a text file:

#     >>> Text.from_file('the_stranger.txt')
# Hint: You need to open and read the text from the text file.


# Now, use the provided the_stranger.txt file and try using the class you created above.


# Bonus:
# Create a class called TextModification that inherits from Text.

# Implement the following methods:
# a method that returns the text without any punctuation.
# a method that returns the text without any english stop-words (check out what this is !!).
# a method that returns the text without any special characters.
# Note: Feel free to implement/create any attribute, method or function needed to make this work, be creative :)


class Text:
    def __init__(self, user_string):
        self.string_list = user_string.lower().split(" ")
        self.string_long = user_string

    def word_frequency(self, user_word):
        return self.string_list.count(user_word.lower())

    def most_common_word(self):
        most_common = ""
        counter = 0
        for item in self.string_list:
            if self.string_list.count(item.lower()) > counter:
                counter = self.string_list.count(item.lower())
                most_common = item.lower()
        return most_common

    def list_unique_words(self):
        self.string_set = list(set(self.string_list))
        return self.string_set

    @classmethod
    def from_file(cls, file_name):
        file_string = ""
        with open(f"./{file_name}", "r") as file_1:
            for line in file_1:
                file_string = file_string + line[:-1]
            return cls(file_string)


new_text = Text("A good book would sometimes cost as much as a good house.")
print(new_text.word_frequency("book"))
print(new_text.most_common_word())
print(new_text.list_unique_words())
the_stranger = Text.from_file("the_stranger.txt")
print(the_stranger.most_common_word())
print(the_stranger.word_frequency("stranger"))
import re
from nltk.corpus import stopwords


class TextModification(Text):
    def __init__(self, user_string):
        super().__init__(user_string)

    def remove_punctuation(self):
        REGEX = r"[^\w\s]"
        return re.sub(REGEX, "", self.string_long)

    def remove_english_stop(self):
        pattern = re.compile(r"\b(" + r"|".join(stopwords.words("english")) + r")\b\s*")
        return pattern.sub("", self.string_long)

    def remove_special_chars(self):
        REGEX = r"[^a-zA-Z0-9 ]"
        return re.sub(REGEX, "", self.string_long)


the_stranger_new = TextModification.from_file("the_stranger.txt")
print(the_stranger_new.remove_english_stop())
