#!/usr/bin/env python3
"""celsius_to_fahrenheit.py"""

# This code converts Celsius temperatures from -44-106 in increments of 4-
#  (including 106 at the end) into Fahrenheit and prints the values side by side -
#  in a table. Code is modified from that given by Dr. David Biersach in
#  fahrenheit_to_celsius.py


def main() -> None:
    """Convert Celsius to Fahrenheit"""
    # Range of Celsius values from -44-104 degrees, increments of 4
    # For loop runs for this range
    for celsius in range(-44, 108, 4):
        # Float= variable type so that I can include decimal points to 2 places
        # Use equation to  convert celsius values to equivalent fahrenheit
        fahrenheit: float = (celsius * 9 / 5) + 32
        # Print table of celsius = fahrenheit values with two decimal places
        print(f"{celsius:>6.2f} C = {fahrenheit:>6.2f} F")
        # Convert 106 degrees celsius into fahrenheit with the same steps as above
    for celsius in range(106, 107, 1):
        # add 106 to the printed table
        fahrenheit_106: float = (celsius * 9 / 5) + 32
        print(f"{celsius:>6.2f} C = {fahrenheit_106:>6.2f} F")


if __name__ == "__main__":
    # Call the main function (conversion function above)
    main()
