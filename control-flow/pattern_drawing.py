# pattern_drawing.py
# Draw a square pattern of '*' using a while loop (rows) and a nested for loop (columns).

# Ask the user for a positive whole number and keep asking until they give one
while True:
    raw = input("Enter the size of the pattern: ").strip()
    try:
        size = int(raw)
        if size > 0:
            break
        else:
            print("Please enter a positive number (like 1, 2, 3).")
    except ValueError:
        print("Please type a whole number (like 4).")

# Use a while loop to go through each row
row = 0
while row < size:
    # For each row, print 'size' stars side-by-side
    for col in range(size):
        print("*", end="")   # print star but stay on same line
    print()                 # move to the next line after the row is done
    row += 1                # go to the next row
