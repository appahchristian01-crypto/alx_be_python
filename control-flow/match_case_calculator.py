# match_case_calculator.py
# A simple calculator that uses a match-case statement (Python 3.10+)

def main():
    print("Simple calculator (use +, -, *, /)\n")

    # 1) Get the two numbers from the user
    try:
        num1 = float(input("Enter the first number: ").strip())
        num2 = float(input("Enter the second number: ").strip())
    except ValueError:
        print("Please enter valid numbers (like 3 or 4.5).")
        return

    # 2) Ask for the operation
    op = input("Choose the operation (+, -, *, /): ").strip()

    # 3) Use match-case to perform the chosen operation
    result = None

    match op:
        case "+":
            result = num1 + num2
        case "-":
            result = num1 - num2
        case "*":
            result = num1 * num2
        case "/":
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                result = num1 / num2
        case _:
            print("Unknown operation. Please choose +, -, * or /.")

    # 4) Print the result if we have one
    if result is not None:
        print("The result is", result)

if __name__ == "__main__":
    main()
