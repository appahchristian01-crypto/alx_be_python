"""
hours_to_seconds.py

Simple script that converts a number of hours into seconds.
Expected output (with hours = 2):

2 hour(s) is 7200 seconds

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

hours = 5   # example input
seconds = hours * 3600
print(seconds)





