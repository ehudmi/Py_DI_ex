# Exercise 1 : Call History
# Instructions
# Create a class called Phone. This class takes a parameter called phone_number. When instantiating an object
# create an attribute called call_history which value is an empty list.

# Add a method called call that takes both self and other_phone (i.e another Phone object) as parameters.
# The method should print a string stating who called who, and add this string to the phone’s call_history.

# Add a method called show_call_history. This method should print the call_history.

# Add another attribute called messages to your __init__() method which value is an empty list.

# Create a method called send_message which is similar to the call method. Each message should be saved as a
# dictionary with the following keys:
# to : the number of another Phone object
# from : your phone number (also a Phone object)
# content

# Create the following methods: show_outgoing_messages(self), show_incoming_messages(self), show_messages_from(self)

# Test your code !!!


class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self, other_phone):
        print(f"{self.phone_number} called {other_phone.phone_number}")
        self.call_history.append(
            f"{self.phone_number} called {other_phone.phone_number}"
        )

    def show_call_history(self):
        print(self.call_history)

    def send_message(self, other_phone, content):
        self.messages.append(
            {
                "to": other_phone.phone_number,
                "from": self.phone_number,
                "content": {content},
            }
        )

    def show_outgoing_messages(self):
        for i in range(0, len(self.messages)):
            print(self.messages[i])

    def show_incoming_messages(self):
        for i in range(0, len(self.messages)):
            if self.messages[i]["to"] == self.phone_number:
                print(self.messages[i])

    def show_messages_from(self):
        for i in range(0, len(self.messages)):
            if self.messages[i]["from"] == self.phone_number:
                print(self.messages[i])


my_phone = Phone("058-6242-585")
my_friend_phone = Phone("054-8344-211")
my_other_friend = Phone("050-7652-424")

my_phone.call(my_friend_phone)
my_phone.call(my_other_friend)
my_friend_phone.call(my_other_friend)
my_friend_phone.call(my_phone)
my_other_friend.call(my_phone)

my_phone.show_call_history()
