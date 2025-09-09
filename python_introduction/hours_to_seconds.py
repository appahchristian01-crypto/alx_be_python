"""
hours_to_seconds.py

Simple script that converts a number of hours into seconds.
Expected output (with hours = 2):

2 hour(s) is 7200 seconds.

This file also contains a step-by-step breakdown written for a 10-year-old.
"""

# 1) Set how many hours you want to convert
hours = 2

# 2) How many seconds are in one hour?
#    1 hour = 60 minutes, and each minute = 60 seconds
#    so 1 hour has 60 * 60 = 3600 seconds
seconds_per_hour = 60 * 60  # equals 3600

# 3) Multiply the number of hours by seconds per hour
seconds = hours * seconds_per_hour

# 4) Print the result in the required format
print(f"{hours} hour(s) is {seconds} seconds.")


# ======================================================
# Step-by-step breakdown for a 10-year-old
# ======================================================
# 1) What is a variable?
#    A variable is like a labeled jar where we can store a number or a word.
#    Here the jar named `hours` holds the number of hours (we put 2 inside).
#
# 2) How many seconds are in an hour?
#    - One hour = 60 minutes.
#    - One minute = 60 seconds.
#    So to find seconds in an hour we do: 60 x 60 = 3600.
#    We put that number in the jar called `seconds_per_hour`.
#
# 3) How do we find seconds for 2 hours?
#    If 1 hour = 3600 seconds, then 2 hours = 2 x 3600.
#    The computer does that multiplication for us and stores it in `seconds`.
#
# 4) Showing the answer
#    We use `print()` to tell the computer to write the sentence on the screen.
#    The sentence follows the format: [hours] hour(s) is [seconds] seconds.
#
# Short analogy:
#    Imagine each hour is a box that holds 3600 candies (seconds).
#    If you have 2 boxes, you have 2 x 3600 candies = 7200 candies.
#
# How to run this file:
#    - Save it as hours_to_seconds.py
#    - Open a terminal/command prompt in the same folder
#    - Run: python hours_to_seconds.py
#
# You should see:
#    2 hour(s) is 7200 seconds.
#
# That's it — simple math + variables = magic! :)
