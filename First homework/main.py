from menufunctions import *
from customer import Customer
from bank import Bank
from account import Account
import account



b = Bank()
b.add_customer("Delmon", "121212")
b.add_customer("Erik","131313")
b.add_customer("Jack", "191919")
# menu()

print(b.add_account("131313"))
print(b.add_account("191919"))
print(b.add_account("131313"))
b.get_customer_by_ssn("131313")
b.deposit(131313,111111,500)
# print(b.remove_customer("131313"))
