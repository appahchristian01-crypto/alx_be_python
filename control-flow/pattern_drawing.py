# pattern_drawing.py

# Ask the user for a positive integer
size = int(input("Enter the size of the pattern: "))

# Start with the first row
row = 0

# Use a while loop to go through each row
while row < size:
    # Use a for loop to print stars in the row
    for col in range(size):
        print("*", end="")
    print()  # move to the next line after finishing the row
    row += 1
