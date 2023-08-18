# Instructions :
# Consider this list

# french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
# Look at this result :
# {"Bonjour": "Hello", "Au revoir": "Goodbye", "Bienvenue": "Welcome", "A bientôt": "See you soon"}
# You have to recreate the result using a translator module. Take a look at the googletrans module

import googletrans

gt = googletrans.Translator()

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
translated = []


def french_translate(words):
    for word in words:
        temp = gt.translate(word, "en", "fr")
        # print(temp)
        translated.append({word: temp.text})
    return translated


french_translate(french_words)
print(translated)
