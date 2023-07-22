#!/usr/bin/env python3
"""herons_method.py"""

# This code implements Heron's method for estimating square roots.
# Code is modified from that given by
# Dr. David Biersach in herons_formula.py.

# Import the random integer function from the library "random."
from random import randint

# Import the mean function from the library "numpy."
from numpy import mean


def main() -> None:  # Defines an entry point for the function.
    # Defines random integer "s" between 10^6 and 2(10^6) that
    # we will calculate the square root of
    s: float = randint(10**6, 2 * 10**6)
    # Initial guess of sqrt s
    x: float = s / 2
    # What our updated guess for sqrt s will be based on x
    x_revised = float(mean([s / x, x]))
    # Calculates the error of the function based on s and x_revised
    error: float = abs(s - x_revised**2)

    while error > 10**-8:  # While error is greater than the acceptable value (10^-8)
        x = x_revised  # x is updated based on x_revised
        # x_revised is updated based on the old value for x_revised.
        x_revised = float(mean([s / x_revised, x_revised]))
        # Error is updated based on the old value for x_revised.
        error = abs(s - x_revised**2)

    r: float = x_revised
    # Rounds r to 8 digits. Used https://realpython.com/python-rounding/ to find
    # Sqrt of s is defined as a floating type r, which is equal to the
    # x_revised that generates an error <10^-8
    r = round(r, 8)
    print(f"The square root of {s:,} is {r:,}")


if __name__ == "__main__":
    # Calls the main function.
    main()
