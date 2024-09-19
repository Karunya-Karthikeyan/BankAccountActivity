
import random
class BankAccount:
    bank_title = "Citizen's Bank"

    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self.account_num = random.randint(0, 20)

    def deposit(self, amount):
        self.current_balance += amount

    def withdrawal(self, amount):
        if amount > self.current_balance - self.minimum_balance:
            print("Your current balance is not enough for withdrawal.")
        else:
            self.current_balance = self.current_balance - amount
        return self.current_balance

    def print_customer_information(self):
        print("Bank Name: " + BankAccount.bank_title + "\nCustomer Name: " + self.customer_name + "\nCurrent Balance: " +
              str(self.current_balance) + "\nMinimum Balance: " + str(self.minimum_balance) + "\nBank account number: "
              + str(self.account_num))
