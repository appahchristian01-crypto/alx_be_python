# explore_datetime.py
# Simple script to show current datetime and compute a future date.

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Get the current date and time, save it into `current_date`,
    format it like 'YYYY-MM-DD HH:MM:SS', print it and return it.
    """
    current_date = datetime.now()                 # save the current date/time
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted}")
    return current_date

def calculate_future_date(days):
    """
    Add `days` to the current date, save the result in `future_date`,
    print the future date as 'YYYY-MM-DD', and return it.
    """
    current_date = datetime.now()                 # start from now
    future_date = current_date + timedelta(days=days)  # add days
    formatted = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted}")
    return future_date

def main():
    # Part 1: show current datetime
    display_current_datetime()

    # Part 2: ask the user how many days to add
    while True:
        user_input = input("Enter the number of days to add to the current date: ").strip()
        try:
            days = int(user_input)   # convert to whole number
            break
        except ValueError:
            print("That is not a whole number. Please type a number like 10 or -3.")

    # calculate and show the future date
    calculate_future_date(days)

if __name__ == "__main__":
    main()
