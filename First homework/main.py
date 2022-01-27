from menu import *
from customer import Customer
from bank import Bank
from account import Account
import account



#menu()
b = Bank()
print(b.add_customer("delmon", 9393939393))
print(b.add_account(9393939393))
print(b.add_account(9393939393))
print(b.get_customers())
print(b.deposit(9393939393,1001,500))
print(b.deposit(9393939393,1002,500))
print(b.close_account(9393939393, 1001))
