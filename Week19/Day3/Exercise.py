people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
# Using map and filter, try to say hello to everyone who's name is less than or equal to 4 letters


def hello(list):
    list_filtered = filter(lambda s: len(s) <= 4, list)
    new_list = map(lambda s: f"Hello {s}", list_filtered)
    for item in new_list:
        print(item)


hello(people)

# Given a list of numbers, write a function that returns the sum of every number. BUT you can have a malicious string inside the list.

my_list = [2, 3, 1, 2, "four", 42, 1, 5, 3, "imanumber"]
sum_list = 0
for item in my_list:
    try:
        sum_list += item
    except:
        continue
print(sum_list)
