
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


account1 = BankAccount("Max", 500.0, 200.0)
account2 = BankAccount("Ben", 500.0, 150.0)

# Test account1
print("\nAccount 1:")
account1.deposit(0)
account1.withdrawal(301.0) # Should fail due to insufficient funds
account1.print_customer_information()

# Test account2
print("\nAccount 2:")
account2.deposit(200.0)
account2.withdrawal(100.0)
account2.print_customer_information()