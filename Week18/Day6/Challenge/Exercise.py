# Challenge 1
# Ask a user for a word
# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.

# Make sure the letters are the keys.
# Make sure the letters are strings.
# Make sure the indexes are stored in a list and those lists are values.
# Examples

# "dodo" ➞ { "d": [0, 2], "o": [1, 3] }

# "froggy" ➞ { "f":  [0], "r": [1], "o": [2], "g": [3, 4], "y": [5] }

# "grapes" ➞ { "g": [0], "r": [1], "a": [2], "p": [3]}

# user_word = input("Please enter a word ")
# word_dict = {}
# key_list = [char for char in user_word]

# for item in key_list:
#     temp_list = [user_word.index(item)]
#     word_dict[item] = temp_list
#     if user_word.count(item) > 1:
#         counter = 1
#         while user_word.count(item) > counter:
#             temp_list.append(user_word.index(item, temp_list[-1]))
#             counter += 1
#         word_dict[item] = temp_list
#     else:
#         word_dict[item] = temp_list
# print(word_dict)

# Challenge 2
# Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
# Sort the list in alphabetical order.
# Return “Nothing” if you can’t afford anything from the store.
# Examples

# The key is the product, the value is the price

# items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}

# wallet = "$300"

# ➞ ["Bread", "Fertilizer", "Water"]

# items_purchase = {
#     "Apple": "$4",
#     "Honey": "$3",
#     "Fan": "$14",
#     "Bananas": "$4",
#     "Pan": "$100",
#     "Spoon": "$2",
# }

# wallet = "$100"

# ➞ ["Apple", "Bananas", "Fan", "Honey", "Pan", "Spoon"]

items_purchase = {
    "Phone": "$999",
    "Speakers": "$300",
    "Laptop": "$5,000",
    "PC": "$1200",
}

wallet = "$1"

# ➞ "Nothing"

affordable_items = []
for k, v in items_purchase.items():
    if items_purchase[k].find(",") > 0:
        items_purchase[k] = items_purchase[k].replace(",", "")
    if int(items_purchase[k][1:]) <= int(wallet[1:]):
        affordable_items.append(k)
if (len(affordable_items)) == 0:
    print("Nothing")
else:
    print(sorted(affordable_items))
