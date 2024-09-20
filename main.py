from BankAcct import BankAccount
from savings_Acct import savings_Acct
from checking_Acct import checking_Acct

# scenario starts
# Instance 1 (Bank Account)
Customer_1 = BankAccount("John", 3000, 500)
Customer_1.deposit(500)
Customer_1.withdrawal(3500)
Customer_1.print_customer_information()
print()
# Instance 2 (Bank Account)
customer_2 = BankAccount("Doe", 4000, 1000)
customer_2.deposit(1000)
customer_2.withdrawal(500)
customer_2.print_customer_information()
print()
print()
Customer_1.transfer(customer_2, 100)
Customer_1.print_customer_information()
print()
customer_2.print_customer_information()
print()
print()
# scenario ends



