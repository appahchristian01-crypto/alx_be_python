# These are like math rules we use for converting temperatures
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
CELSIUS_TO_FAHRENHEIT_OFFSET = 32

# This function turns Fahrenheit into Celsius
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - CELSIUS_TO_FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# This function turns Celsius into Fahrenheit
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + CELSIUS_TO_FAHRENHEIT_OFFSET
    return fahrenheit

# This is where we talk to the person using the program
def main():
    try:
        # Ask the user to type a number for the temperature
        temperature = float(input("Enter the temperature to convert: "))
        
        # Ask if it's in Celsius or Fahrenheit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # If they typed 'C', we turn it into Fahrenheit
        if unit == 'C':
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {result}°F")
        
        # If they typed 'F', we turn it into Celsius
        elif unit == 'F':
            result = convert_to_celsius(temperature)
            print(f"{temperature}°F is {result}°C")
        
        # If they didn't type C or F, we tell them it's wrong
        else:
            print("Please type only 'C' for Celsius or 'F' for Fahrenheit.")
    
    # If they type something that isn’t a number, we show an error
    except ValueError:
        print("Invalid temperature. Please enter a number like 25 or 98.6")

# This tells Python to run the program
if __name__ == "__main__":
    main()
