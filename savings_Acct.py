import math
import random
from BankAcct import BankAccount

class savings_Acct(BankAccount):

    def __init__(self, customer_name, current_balance, minimum_balance, interest_rate):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.interest_rate = interest_rate
        self.year = 0

    def addYears(self, years):
        self.year += years

    def calculateInterest(self):
        self.current_balance = round(self.current_balance*(math.pow((1 + self.interest_rate), self.year)), 2)

    def print_Customer_Information(self):
        print("\nName: " + self.customer_name + "\nCurrent Balance: " + self.current_balance +
              "\nSavings Account account number: " + self.account_num + "\nInterest rate: " + self.interest_rate +
              "\nYears: " + self.year + " year(s)")