# bank_account.py
class BankAccount:
    def __init__(self, balance=0):
        # This starts the account with some money (default 0)
        self.account_balance = balance

    def deposit(self, amount):
        # Put money in the account
        self.account_balance += amount

    def withdraw(self, amount):
        # Take money out if there is enough
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        # Show how much money is in the account
        print(f"Current Balance: ${self.account_balance}")
