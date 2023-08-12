# Exercise 1: Bank Account
# Instructions
# Part I:

# Create a class called BankAccount that contains the following attributes and methods:
# balance - (an attribute)
# __init__ : initialize the attribute
# deposit : - (a method) accepts a positive int and adds to the balance, raise an Exception if the int is not positive.
# withdraw : - (a method) accepts a positive int and deducts from the balance, raise an Exception if not positive


class BankAccount:
    def __init__(self, balance, name, password):
        self.balance = balance
        self.username = name
        self.password = password
        self.authenticated = False

    def deposit(self, sum):
        if self.authenticated == True:
            if sum < 0:
                raise Exception("The deposited sum is less than 0")
            else:
                self.balance += sum
        else:
            raise Exception("User not authenticated")

    def withdraw(self, sum):
        if self.authenticated == True:
            self.balance -= sum
            if self.balance < 0:
                raise Exception("The balance is less than 0")
        else:
            raise Exception("User not authenticated")

    def authenticate(self, name, password):
        if self.username == name and self.password == password:
            self.authenticated = True


# Part II : Minimum balance account

# Create a MinimumBalanceAccount that inherits from BankAccount.
# Extend the __init__ method and accept a parameter called minimum_balance with a default value of 0.
# Override the withdraw method so it only allows the user to withdraw money if the balance remains higher than the
# minimum_balance, raise an Exception if not.


class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance, name, password):
        super().__init__(balance, name, password)
        self.minimum_balance = 0

    def withdraw(self, sum):
        if self.balance - sum > self.minimum_balance:
            self.balance -= sum
        else:
            raise Exception("You can't withdraw. Not enough Funds")


# Part III: Expand the bank account class

# Add the following attributes to the BankAccount class:
# username
# password
# authenticated (False by default)

# Create a method called authenticate. This method should accept 2 strings : a username and a password.
# If the username and password match the attributes username and password the method should set the authenticated
# boolean to True.

# Edit withdraw and deposit to only work if authenticated is set to True, if someone tries an action without
# being authenticated raise an Exception


# Part IV: BONUS Create an ATM class


class ATM:
    def __init__(self, account_list, try_limit):
        super().__init__()
        try:
            isinstance(account_list, (BankAccount, MinimumBalanceAccount))
            self.account_list = account_list
        except:
            print("This is not a valid list")
        try:
            if try_limit > 0:
                self.try_limit = try_limit
        except:
            print("The value you input is not positive")
            self.try_limit = 2
        self.current_tries = 0

    def show_main_menu(self):
        self.exit_flag = False
        while self.exit_flag == False:
            if input("Please select Login or Exit ") == "login":
                self.login(
                    input("Please enter user name "),
                    input("Please enter password "),
                )
            else:
                self.exit_flag = True

    def login(self, name, password):
        for item in self.account_list:
            item.authenticate(name, password)
            if item.authenticated == True:
                self.account = item
                self.show_account_menu(self.account)
                return
        self.current_tries += 1
        if self.current_tries == self.try_limit:
            print("You have reached maximum attempts. Goodbye!!")
            self.exit_flag = True

    def show_account_menu(self, account):
        self.account_exit = False
        while self.account_exit == False:
            user_input = input("Please select Deposit or Withdraw or Exit ")
            if user_input == "exit":
                self.exit_flag = True
                self.login(account.username, account.password)
            elif user_input == "deposit":
                self.account.deposit(int(input("Please Enter Sum")))
            elif user_input == "withdraw":
                self.account.withdraw(int(input("Please Enter Sum")))


# __init__:
# Accepts the following parameters: account_list and try_limit.

# Validates that account_list contains a list of BankAccount or MinimumBalanceAccount instances.
# Hint: isinstance()

# Validates that try_limit is a positive number, if you get an invalid input raise an Exception, then move
# along and set try_limit to 2.
# Hint: Check out this tutorial

# Sets attribute current_tries = 0

# Call the method show_main_menu (see below)

# Methods:
# show_main_menu:
# This method will start a while loop to display a menu letting a user select:
# Log in : Will ask for the users username and password and call the log_in method with the username and
# password (see below).
# Exit.

# log_in:
# Accepts a username and a password.

# Checks the username and the password against all accounts in account_list.
# If there is a match (ie. use the authenticate method), call the method show_account_menu.
# If there is no match with any existing accounts, increment the current tries by 1. Continue asking the user
# for a username and a password, until the limit is reached (ie. try_limit attribute). Once reached display a message
# saying they reached max tries and shutdown the program.

# show_account_menu:
# Accepts an instance of BankAccount or MinimumBalanceAccount.
# The method will start a loop giving the user the option to deposit, withdraw or exit.

account_1 = BankAccount(300, "Ehud", "elric120")
account_2 = BankAccount(150, "Moshe", "123456")
account_3 = BankAccount(0, "Haim", "Haim1234")
account_4 = MinimumBalanceAccount(200, "Jim", "heb362")
account_5 = MinimumBalanceAccount(400, "Joe", "dana78")
account_6 = MinimumBalanceAccount(600, "Pete", "my_cat")
my_atm = ATM([account_1, account_2, account_3, account_4, account_5, account_6], 4)
my_atm.show_main_menu()
