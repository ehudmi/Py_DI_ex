my_age = 56
print(my_age + 123879)

first_name = "Ehud"
last_name = "Miron"
print(first_name + " " + last_name)

cars = 100
# cars = 100  this line creates a cars variable type: integer
# print(f"I have {cars} cars")

space_in_a_car = 4.0
# space_in_a_car = 4.0  this line creates a space_in_a_car variable type: float
# print(f"There's room for {space_in_a_car} people")

drivers = 30
# drivers = 30  this line creates a drivers variable type: integer
# print(f"There are {drivers} drivers in the company")

passengers = 90
# passengers = 90  this line creates a passengers variable type: integer
# print(f"There are {passengers} passengers to be driven".)

cars_not_driven = cars - drivers
# cars_not_driven = X  this line creates a cars_not_driven variable type: integer
# print(f"There are {cars_not_driven} cars not driven")

cars_driven = drivers
# cars_driven = X  this line creates a cars_driven variable type: integer
# print(f"There are {cars_driven} cars being driven")

carpool_capacity = cars_driven * space_in_a_car
# carpool_capacity = X  this line creates a carpool_capacity variable type: float
# print(f"The carpool capacity is {carpool_capacity}")

average_passengers_per_car = passengers / cars_driven
# average_passengers_per_car = X  this line creates an average_passengers_per_car variable type: float
# print(f"There are {average_passengers_per_car} passengers per car on average")


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

age = input("Choose a number between 1 and 100 ")
if int(age) % 3 == 0 and int(age) % 5 == 0:
    print("FizzBuzz")
elif int(age) % 3 == 0:
    print("Fizz")
elif int(age) % 5 == 0:
    print("Buzz")
else:
    print("Darn")
