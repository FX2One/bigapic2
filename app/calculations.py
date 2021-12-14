def add(a:int ,b:int ):
    return a + b

def substract(a:int ,b:int ):
    return a - b

def divide(a:int ,b:int ):
    return a / b

def multiply(a:int ,b:int ):
    return a * b

class BankAccount():
    def __init__(self, start_balance=0):
        self.balance = start_balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if amount > self.balance:
            raise Exception("you're trying to withdraw more than you already have")
        self.balance -= amount

    def collect(self):
        self.balance *=1.1

