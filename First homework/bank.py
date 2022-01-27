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
        if self.customer_list == []:
            return "There isn't customers to show"
        else:
            for x in self.customer_list:
                return x.ssn, x.name


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
                        return False



    def withdraw(self, ssn, ac_number, amount):
        for x in self.customer_list:
            if x.ssn == ssn:
                for a in self.account_list:
                    if a.ac_number == ac_number:
                        if a.saldo >= amount:
                            a.saldo -= amount
                            return True
                        else:
                            return False


    def close_account(self, ssn, account_id):
        closed_acc=[]
        ret_saldo= 0.0

        for c in self.customer_list:
            if c.ssn == ssn:
                for a in self.account_list:
                    if a.ac_number == account_id:
                        ret_saldo = a.saldo
                        closed_acc.append(a)
                for s in closed_acc:
                    return f"Account {s} closed\nSaldo to return={ret_saldo}"


