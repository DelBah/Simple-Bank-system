import itertools
class Account:
    ac_number = itertools.count()


    def __init__(self, customer_id):
        self.saldo = 0
        self.ac_type = "Debit account"
        self.ac_number = next(self.ac_number)
        self.ac_number = 1001 + self.ac_number
        self.customer_id = customer_id



    def __str__(self):
        return f":{self.ac_number}:{self.ac_type}:{self.saldo}"

