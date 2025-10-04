# bank_account.py

class BankAccount:
    def __init__(self, balance=0):
        """
        Initialize the bank account with an optional starting balance.
        balance: numeric (int or float). Default is 0.
        """
        self.account_balance = float(balance)

    def deposit(self, amount):
        """
        Add amount to the account balance.
        amount: numeric (int or float)
        """
        self.account_balance += float(amount)

    def withdraw(self, amount):
        """
        Subtract amount from the balance if funds are sufficient.
        Returns True if withdrawal succeeded, False otherwise.
        """
        amount = float(amount)
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """
        Print the current balance formatted with two decimal places.
        This matches the exact expected output like: Current Balance: $250.00
        """
        print(f"Current Balance: ${self.account_balance:.2f}")
