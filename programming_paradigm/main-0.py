# main-0.py
import sys
from bank_account import BankAccount

def main():
    # Start the account with $100 by default (change if needed)
    account = BankAccount(100)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    # Use general formatting for displayed amounts (strip unnecessary .0)
    def fmt(a):
        return f"{a:g}"

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${fmt(amount)}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${fmt(amount)}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
