import itertools


class Customer:
    id = itertools.count()

    def __init__(self, name:str, ssn:str):
        self.id = next(self.id)
        self.id = 111110 + self.id
        self.name = name
        self.ssn = ssn

    def __str__(self):
        return f"{self.id}:{self.name}:{self.ssn}"
