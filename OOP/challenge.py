# Challenge 

"""
Create a bank account class that has two attributes:

* owner
* balance

and two methods:

* deposit
* withdraw

As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
"""

class Account():
    def __init__(self,owner, balance):
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        return f"{self.owner}, ${self.balance}"
    def deposit(self, deposit_amount):
        self.balance = self.balance + deposit_amount
        return str(self)
    def withdraw(self, withdrawal_amount):
        if withdrawal_amount > self.balance:
            print(" Funds Unavailable")
        else:
            self.balance = self.balance - withdrawal_amount
            print("Withdraw accepted")

acc1 = Account('Jose',100)
print(acc1)

print(acc1.owner)
print(acc1.balance)
print(acc1.deposit(50))
print(acc1.withdraw(25))
print(acc1.balance)