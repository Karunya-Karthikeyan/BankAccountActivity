import math
import random
<<<<<<< HEAD
=======

>>>>>>> 5149593 (Initial Commit of files)
from BankAcct import BankAccount

class savings_Acct(BankAccount):

<<<<<<< HEAD
=======
    # constructor method
>>>>>>> 5149593 (Initial Commit of files)
    def __init__(self, customer_name, current_balance, minimum_balance, interest_rate):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.interest_rate = interest_rate
        self.year = 0
<<<<<<< HEAD

    def addYears(self, years):
        self.year += years

    def calculateInterest(self):
        self.current_balance = round(self.current_balance*(math.pow((1 + self.interest_rate), self.year)), 2)

    def print_Customer_Information(self):
        print("\nName: " + self.customer_name + "\nCurrent Balance: " + self.current_balance +
              "\nSavings Account account number: " + self.account_num + "\nInterest rate: " + self.interest_rate +
              "\nYears: " + self.year + " year(s)")
=======
        self.routing_num = random.randint(20, 40)

    # years method
    def addYears(self, years):
        self.year += years

    # Interest Calculation method
    def calculateInterest(self):
        self.current_balance = round(self.current_balance*(math.pow((1 + self.interest_rate), self.year)), 2)

    # info method
    def print_customer_information(self):
        print("\nName: ", self.customer_name, "\nCurrent Balance: ", self.current_balance,
              "\nSavings Account account number: ", self.account_num, "\nSavings Account Routing Number: ", self.routing_num,
              "\nInterest rate: ", self.interest_rate, "\nYears: ", self.year, " year(s)")
>>>>>>> 5149593 (Initial Commit of files)
