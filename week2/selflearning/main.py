class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        self._balance + amount 
    def withdraw(self, amount):
        self._balance -= amount