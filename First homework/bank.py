from customer import Customer
from account import Account
class Bank:
    customer_list = []
    account_list=[]

    def __init__(self):
        pass

    def _load(self):
        list_info=[]
        try:
            f = open ("Customer_bank.txt")
            for x in f:
                line = x.strip().split(":")
                list_info.append(line)
        finally:
            f.close()

        return list_info

    def _load_customers(self):
        data = Bank._load(self)
        try:
            for x in data:
                customer= Customer(x[0],x[1])
                self.customer_list.append(customer)
        except:
            print("something went wrong")


    def get_customers(self):
        ret_list = []

        for x in self.customer_list:
            ret_list.append(x.name)
            ret_list.append(x.ssn)
        return ret_list


    #add a customer to the list
    def add_customer(self, name, ssn):
        c = Customer(name, ssn)
        my_list= self.customer_list
        #this is for the first customer
        #do not need to check if customer exist
        if my_list == []:
            my_list.append(c)
            return "You are a customer now!"
        else:
            #secound value program execut here
            for x in my_list:
                if x.ssn != c.ssn:
                    my_list.append(c)
                    print("You are a customer now!")
                    break
                else:
                    print("A customer with the same ssn already exist!")
                    break

    def get_customer_by_ssn(self, ssn):
        for x in self.customer_list:
            if x.ssn == ssn:
                if self.account_list == []:
                    print("You have not create an account yet!")
                else:
                    for a in self.account_list:
                        if a.customer_id == x.id:
                                print(x.name, x.ssn, a)




    def change_customer_name(self, name, ssn):
        for x in self.customer_list:
            if x.ssn == ssn:
                x.name = name
                print("Your new name", name)
                break
            else:
                return False

    def remove_customer(self, ssn):
        balance = 0.0
        return_list= []
        for x in self.customer_list:
            if x.ssn == ssn:
                index= self.customer_list.index(x)
                self.customer_list.pop(index)

                for a in self.account_list:
                    if a.customer_id == x.id:
                        return_list.append(a)
                        balance += a.saldo
                        return_list.append(balance)
                        index = self.account_list.index(a)
                        self.account_list.pop(index)

                        for s in return_list:
                            return s

    def add_account(self, ssn):
        temp_list = []

        for c in self.customer_list:
            if c.ssn == ssn:
                for a in self.account_list:
                    if a.customer_id == c.id:
                        temp_list.append(a)

                if len(temp_list) == 2:
                    return "You can only have two accounts"
                else:
                    new_acc = Account(c.id)
                    self.account_list.append(new_acc)
                    return new_acc.ac_number


    def get_account(self, ssn, ac_number):
        for c in self.customer_list:
            if c.ssn == ssn:
                for a in self.account_list:
                    if a.ac_number == ac_number:
                        return a

    def deposit(self, ssn, ac_number, amount):
        for x in self.customer_list:
            if x.ssn == ssn:
                for a in self.account_list:
                    if a.ac_number == ac_number:
                        a.saldo += amount
                        return True
                    else:
                        return f"Couldn't find an account with the this account number {ac_number}"





    def withdraw(self, ssn, ac_number, amount):
        for x in self.customer_list:
            if x.ssn == ssn:
                for a in self.account_list:
                    if a.ac_number == ac_number:
                        if a.saldo >= amount:
                            a.saldo -= amount
                            return True
                    else:
                        return f"Couldn't find an account with the this account number {ac_number}"



    def close_account(self, ssn, account_id):
        closed_acc=[]
        ret_saldo= 0.0

        for c in self.customer_list:
            if c.ssn == ssn:
                for a in self.account_list:
                    if a.ac_number == account_id:
                        ret_saldo = a.saldo
                        closed_acc.append(a)
                        self.account_list.remove(a)
                for s in closed_acc:
                    print(f"Account to close {s} \n Saldo to return = {ret_saldo}")


