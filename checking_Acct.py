import random

from BankAcct import BankAccount

class checking_Acct(BankAccount):

    # constructor method
    def __init__(self, customer_name, current_balance, minimum_balance, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.transfer_limit = transfer_limit
        self.routing_num = random.randint(20, 40)

    # withdrawal method
    def withdrawal(self, amount):
        if(amount > self.transfer_limit):
            print("Error: Amount greater than transfer limit")
            return False
        else:
            if self.current_balance - amount < self.minimum_balance:
                print("Error: Minimum balance not met")
                return False
            else:
                print("Withdrawal successful")
                self.current_balance = self.current_balance - amount
                return True

    # transfer method
    def transfer(self, acct2, amount):
            if self.withdrawal(amount):
                acct2.deposit(amount)
            else:
                print("Error: Amount greater than transfer limit")

    # info method
    def print_customer_information(self):
        print("\nName: ", self.customer_name, "\nCurrent Balance: ", self.current_balance,
              "\nSavings Account account number: ", self.account_num, "\nSavings Account Routing Number: ", self.routing_num,
              "\nTransfer Limit : $", self.transfer_limit)