# Instructions
# Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
# Display a little cake as seen below:
#        ___iiiii___
#       |:H:a:p:p:y:|
#     __|___________|__
#    |^^^^^^^^^^^^^^^^^|
#    |:B:i:r:t:h:d:a:y:|
#    |                 |
#    ~~~~~~~~~~~~~~~~~~~

# The number of candles on the cake should be the last number of the users age, if they are 53, then add 3 candles.

# Bonus : If they were born on a leap year, display two cakes !

birth_date = input("What is your birthdate in DD/MM/YYYY format? ")
birth_year = int(birth_date[6:])
user_age = 2023 - birth_year
age_unit = int(str(user_age)[1])
my_cake = f"""
       {"_"*int((11-age_unit)/2)}{"i"*age_unit}{"_"*(11-age_unit-int((11-age_unit)/2))}
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
"""
if birth_year % 4 == 0 and birth_year % 100 != 0:
    print(my_cake * 2)
else:
    print(my_cake)
