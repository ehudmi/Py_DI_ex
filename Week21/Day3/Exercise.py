# Exercise
# Download this text file http://www.practicepython.org/assets/nameslist.txt and do the following steps

# Read the file line by line
# Read only the 5th line of the file
# Read only the 5 first characters of the file
# Read all the file and return it as a list of strings. Then split each word
# Find out how many occurrences of the names "Darth", "Luke" and "Lea" are in the file
# Append your first name at the end of the file
# Append "SkyWalker" next to each first name "Luke"

with open("C:/Github/Python_Bootcamp/Py_DI_ex/Week21/Day3/names.txt", "r") as f1:
    for i in f1:
        print(i)
content = f1.readlines()
print(content[4])
print(f1.readline(5))
content = []
for line in f1:
    content.append(line[:-1])
print(content)
darth_counter = 0
lea_counter = 0
luke_counter = 0
for item in content:
    if item == "Darth":
        darth_counter += 1
    elif item == "Luke":
        luke_counter += 1
    else:
        lea_counter += 1
print(
    f"The name 'Darth' appears {darth_counter} times, 'Luke' appears {luke_counter} times and 'Lea' {lea_counter} times"
)
f1.write("\nEhud")
content = []
for line in f1:
    if line == "Luke\n":
        line = "Luke Skywalker\n"
    content.append(line)
print(content)
with open("C:/Github/Python_Bootcamp/Py_DI_ex/Week21/Day3/names.txt", "w") as f1:
    for item in content:
        f1.writelines(item)

f1.close()

# Exercise
# Create a folder with two files : index.py and file.json. Save this code into the json file
# {
#     "firstName": "Jane",
#     "lastName": "Doe",
#     "hobbies": ["running", "sky diving", "singing"],
#     "age": 35,
#     "children": [
#         {
#             "firstName": "Alice",
#             "age": 6
#         },
#         {
#             "firstName": "Bob",
#             "age": 8
#         }
#     ]
# }


# Retrieve the data into the python file, inside a variable called family
# Print nicely the details about Jane's children
# Inside the family variable, add to each children, a key 'favorite_color' with a value
# Then, save back all the new data into the json file
# Use the indent argument inside the dump function. Check out the documentation and the video in the Useful Resources
# Run the python file

# Exercise
# Use the Chuck Norris API https://api.chucknorris.io/ to retrieve some jokes in a specific category
# Use every notion described in the lesson
