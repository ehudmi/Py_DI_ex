# 🌟 Exercise 1 : Temperature Advice
# Instructions
# Create a function called get_random_temp().
# This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
# Test your function to make sure it generates expected results.

from random import randint


def get_random_temp():
    return randint(-10, 40)


# Create a function called main().
# Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
# Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”


def main():
    rand_temp = get_random_temp()

    if rand_temp < 0:
        print("Brrr, that's freezing! Wear some extra layers today")
    elif 0 <= rand_temp < 16:
        print("Quite chilly! Don't forget your coat")
    elif 16 <= rand_temp <= 23:
        print("Nice weather! Enjoy")
    elif 24 <= rand_temp < 32:
        print("Getting warm! Short sleeves recommended")
    elif 32 <= rand_temp <= 40:
        print("Very hot! Get sunscreen")


main()


# Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
# below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
# between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
# between 16 and 23
# between 24 and 32
# between 32 and 40

# Change the get_random_temp() function:
# Add a parameter to the function, named ‘season’.
# Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper
# limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
# Now that we’ve changed get_random_temp(), let’s change the main() function:
# Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly.
# Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
# Use the season as an argument when calling get_random_temp().


def get_random_temp_new(season):
    if season == "winter":
        return randint(-10, 15)
    elif season == "autumn":
        return randint(16, 22)
    elif season == "spring":
        return randint(23, 31)
    elif season == "summer":
        return randint(32, 40)


# Create a function called main().
# Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
# Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”


def main_new(user_season):
    rand_temp = get_random_temp_new(user_season)
    rand_temp = int(f"{rand_temp}")
    season_selected = user_season
    print(f"The temperature right now is {rand_temp} degrees Celsius.")
    if rand_temp < 0:
        print("Brrr, that's freezing! Wear some extra layers today")
    if season_selected == "winter":
        print("Quite chilly! Don't forget your coat")
    elif season_selected == "autumn":
        print("Nice weather! Enjoy")
    elif season_selected == "spring":
        print("Getting warm! Short sleeves recommended")
    else:
        print("Very hot! Get sunscreen")


main_new(input("Please elect a season "))

# Bonus: Give the temperature as a floating-point number instead of an integer.

# Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December).
# Determine the season according to the month.

from random import uniform


def get_random_temp_newest(month):
    if 1 <= month < 3 or 11 <= month <= 12:
        return round(uniform(-10, 15), 2)
    elif 9 <= month < 11:
        return round(uniform(16, 22), 2)
    elif 3 <= month < 6:
        return round(uniform(23, 31), 2)
    elif 6 <= month < 9:
        return round(uniform(32, 40), 2)


def main_newest(user_month):
    rand_temp = get_random_temp_newest(user_month)
    rand_temp = float(f"{rand_temp}")

    print(f"The temperature right now is {rand_temp} degrees Celsius.")
    if rand_temp < 0:
        print("Brrr, that's freezing! Wear some extra layers today")
    elif 0 <= rand_temp < 16:
        print("Quite chilly! Don't forget your coat")
    elif 16 <= rand_temp <= 23:
        print("Nice weather! Enjoy")
    elif 24 <= rand_temp < 32:
        print("Getting warm! Short sleeves recommended")
    elif 32 <= rand_temp <= 40:
        print("Very hot! Get sunscreen")


main_newest(int(input("Please elect a month - 1 - to 12 ")))

# 🌟 Exercise 2 : Star Wars Quiz
# Instructions
# This project allows users to take a quiz to test their Star Wars knowledge.
# The number of correct/incorrect answers are tracked and the user receives different messages depending on how
# well they did on the quiz.

# Here is an array of dictionaries, containing those questions and answers

data = [
    {"question": "What is Baby Yoda's real name?", "answer": "Grogu"},
    {"question": "Where did Obi-Wan take Luke after his birth?", "answer": "Tatooine"},
    {"question": "What year did the first Star Wars movie come out?", "answer": "1977"},
    {"question": "Who built C-3PO?", "answer": "Anakin Skywalker"},
    {"question": "Anakin Skywalker grew up to be who?", "answer": "Darth Vader"},
    {"question": "What species is Chewbacca?", "answer": "Wookiee"},
]


# Create a function that asks the questions to the user, and check his answers. Track the number of correct,
# incorrect answers. Create a list of wrong_answers
# Create a function that informs the user of his number of correct/incorrect answers.
# Bonus : display to the user the questions he answered wrong, his answer, and the correct answer.
# If he had more then 3 wrong answers, ask him to play again.

incorrect_list = []


def check_answer(answer, data_index):
    if answer == data[data_index]["answer"]:
        return True
    else:
        incorrect_list.append(
            {
                "question": data[data_index]["question"],
                "right_answer": data[data_index]["answer"],
                "your_answer": answer,
            }
        )
        return False


def ask_question():
    incorrect_answers = 0
    correct_answers = 0
    for index in range(0, 5):
        print(data[index]["question"])
        user_answer = input("What is your answer? ")
        if check_answer(user_answer, index) == True:
            correct_answers += 1
        else:
            incorrect_answers += 1
            if incorrect_answers >= 3:
                print("You have answered 3 questions wrong - please play again")
                break
    print(
        f"You have answered {correct_answers} questions correctly and {incorrect_answers} questions wrong"
    )
    for index in range(0, len(incorrect_list) - 1):
        print(
            f"you have answered the question {incorrect_list[index]['question']} with the answer {incorrect_list[index]['your_answer']} and the right answer is {incorrect_list[index]['right_answer']}"
        )


ask_question()

# Exercise 3 : When Will I Retire ?
# Instructions
# The point of the exercise is to check if a person can retire depending on their age and their gender.
# Note : Let’s say retirement age is 67 for men, and 62 for women (born after April, 1947).

# Create a function get_age(year, month, day)
# Hard-code the current year and month in your code (there are better ways of doing this,
# but for now it will be enough.)
# After calculating the age of a person, the function should return the age (the age is an integer).
# Create a function can_retire(gender, date_of_birth).
# It should call the get_age function (with what arguments?) in order to receive an age.
# Now it has all the information it needs in order to determine if the person with the given gender and
# date of birth is able to retire or not.
# Calculate. You may need to do a little more hard-coding here.
# Return True if the person can retire, and False if he/she can’t.
# Some Hints

# Ask for the user’s gender as “m” or “f”.
# Ask for the user’s date of birth in the form of “yyyy/mm/dd”, eg. “1993/09/21”.
# Call can_retire to get a definite value for whether the person can or can’t retire.
# Display a message informing the user whether they can retire or not.
# As always, test your code to ensure it works.


def get_age(year, month, day):
    current_year = 2023
    current_month = 8
    current_day = 5
    if current_month >= month and current_day >= day:
        return current_year - year
    else:
        return current_year - year - 1


def can_retire(gender, date_of_birth):
    age = get_age(
        int(date_of_birth[0:4]), int(date_of_birth[5:7]), int(date_of_birth[8:10])
    )
    if age >= 62 and gender == "f":
        print(f"Lady - You can retire - your age is {age}")
    elif age >= 67 and gender == "m":
        print(f"Sir - You can retire - your age is {age}")
    else:
        print(f"Sorry - You cannot retire yet - your age is {age}")


can_retire(
    input("Are you male or female? - answer m or f "),
    input("What is your date of birth? in YYYY/MM/DD format "),
)

# Exercise 4:
# Instructions
# Write a function that accepts one parameter (an int: X) and returns the value of X+XX+XXX+XXXX.
# Example:

# If X=3, the output when calling our function should be 3702 (3 + 33 + 333 + 3333)

# Hint: treating our number as a int or a str at different points in our code may be helpful


def play_with_integer(user_int):
    num_list = []
    for i in range(0, 4):
        num_list.append(user_int * (10**i))
        if i > 0:
            num_list[i] = num_list[i] + num_list[i - 1]
    print(sum(num_list))


play_with_integer(int(input("Please select a digit between 1 and 9 3 ")))
