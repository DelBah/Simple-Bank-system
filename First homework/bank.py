from customer import Customer
from account import Account
class Bank:
    customer_list = []
    account_list=[]

    def __init__(self):
        pass

    # def load(self):
        #kod here

    def get_customers(self):
        for x in self.customer_list:
            print(x.ssn,x.name)


    #add a customer to the list
    def add_customer(self, name, ssn):
        c = Customer(name, ssn)
        my_list= self.customer_list
        #this is for the first customer
        #do not need to check if customer exist
        if my_list == []:
            my_list.append(c)
            print("You are a customer now!")
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
                print(x.name, x.ssn)

    def change_customer_name(self, name, ssn):
        for x in self.customer_list:
            if x.ssn == ssn:
                x.name = name
                print("Your new name", name)
                break

    def remove_customer(self, ssn):
        for x in self.customer_list:
            if x.ssn == ssn:
                self.customer_list.remove(x)
                print("Removing accomplish")
                break
    def add_account(self, ssn):
        temp_list = []

        for c in self.customer_list:
            if c.ssn == ssn:
                for a in self.account_list:
                    if a.customer_id == c.id:
                        temp_list.append(a)

                if len(temp_list) == 2:
                    return -1
                elif len(temp_list) == 1:
                    new_acc = Account(c.id)
                    self.account_list.append(new_acc)
                    return new_acc.ac_number
                else:
                    new_acc = Account(c.id)
                    self.account_list.append(new_acc)
                    return new_acc.ac_number


    def get_account(self,ssn, account_id):
        for c in self.customer_list:
            if c.ssn == ssn:
                for a in self.account_list:
                    if a.customer_id == account_id:
                        print(a)

    def deposit(self, ssn, account_id, amount):
        for x in self.customer_list:
            if x.ssn == ssn:
                for a in self.account_list:
                    if a.customer_id == account_id:
                        a.saldo += amount
                        return True
                    else:
                        return False


    def withdraw(self, ssn, account_id, amount):
        for x in self.customer_list:
            if x.ssn == ssn:
                for a in self.account_list:
                    if a.customer_id == account_id:
                        if a.saldo >= amount:
                            a.saldo -= amount
                            return True
                        else:
                            return False


    # def close_account(self, ssn, account_id):
            #kod here