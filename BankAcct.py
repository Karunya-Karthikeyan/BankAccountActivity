<<<<<<< HEAD

import random
class BankAccount:
    bank_title = "Citizen's Bank"

=======
import random

class BankAccount:
    # class attribute
    bank_title = "Bank of America"

    # constructor method
>>>>>>> 5149593 (Initial Commit of files)
    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self.account_num = random.randint(0, 20)
<<<<<<< HEAD

    def deposit(self, amount):
        self.current_balance += amount

=======
        self.routing_num = random.randint(20, 40)

    # deposit method
    def deposit(self, amount):
        self.current_balance += amount

    # withdrawal method (remaining_balance = current_balance - amount)
>>>>>>> 5149593 (Initial Commit of files)
    def withdrawal(self, amount):
        if amount > self.current_balance - self.minimum_balance:
            print("Your current balance is not enough for withdrawal.")
        else:
            self.current_balance = self.current_balance - amount
        return self.current_balance

<<<<<<< HEAD
    def print_customer_information(self):
        print("Bank Name: " + BankAccount.bank_title + "\nCustomer Name: " + self.customer_name + "\nCurrent Balance: " +
              str(self.current_balance) + "\nMinimum Balance: " + str(self.minimum_balance) + "\nBank account number: "
              + str(self.account_num))
=======
    # info method
    def print_customer_information(self):
        print("Bank Name: " + BankAccount.bank_title + "\nCustomer Name: " + self.customer_name + "\nCurrent Balance: " +
              str(self.current_balance) + "\nMinimum Balance: " + str(self.minimum_balance) + "\nBank account number: "
              + str(self.account_num) + "\nBank Routing Number: " + str(self.routing_num))

    # transfer method
    def transfer(self, acct2, amount):
        if self.withdrawal(amount):
            acct2.deposit(amount)
>>>>>>> 5149593 (Initial Commit of files)
