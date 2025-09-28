# temp_conversion_tool.py

# Global conversion factors (exact names expected by the tests)
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    Accepts numeric values or strings that can be converted to float.
    Raises ValueError("Invalid temperature. Please enter a numeric value.") on bad input.
    """
    try:
        f = float(fahrenheit)
    except (TypeError, ValueError):
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    return (f - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    Accepts numeric values or strings that can be converted to float.
    Raises ValueError("Invalid temperature. Please enter a numeric value.") on bad input.
    """
    try:
        c = float(celsius)
    except (TypeError, ValueError):
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    return (c * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    """Interactive user flow (kept inside main so importing this module doesn't block tests)."""
    raw_temp = input("Enter the temperature to convert: ").strip()
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "F":
        result = convert_to_celsius(raw_temp)  # will raise ValueError on bad numeric input
        print(f"{float(raw_temp)}°F is {result}°C")
    elif unit == "C":
        result = convert_to_fahrenheit(raw_temp)  # will raise ValueError on bad numeric input
        print(f"{float(raw_temp)}°C is {result}°F")
    else:
        # invalid unit -> explicit error
        raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
