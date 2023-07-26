user_string = input("Write a 10 character string ")

if len(user_string) == 10:
    print("perfect string")
elif len(user_string) < 10:
    print("string not long enough")
else:
    print("string too long")

print(user_string[0] + " " + user_string[-1])

for i in user_string:
    print(i)

from random import shuffle

new_string = list(user_string)
shuffle(new_string)
print("".join(new_string))
