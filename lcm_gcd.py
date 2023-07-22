#!/usr/bin/env python3
"""lcm_gcd.py"""

# This code displays the lowest common multiple of 447618 and 2011825.
# Code is modified from that given by
# Dr. David Biersach in euclid_gcd.py and coprime_probability.py.

# imports the function for finding the greatest common factor from the library math
from math import gcd


def main() -> None:  # defines an entry point for the program
    a: int = 447618  # first integer to test, "a", is defined
    b: int = 2011835  # second integer is defined
    greatest = gcd(
        a, b
    )  # The greatest common factor is defined as "greatest" using gcd
    # The least common factor is equal to the product of two integers divided by the gcd
    lesser = (a * b) / greatest
    # Prints a and b and their least common factor.
    print(f"The lowest common multiple of {a:,} and {b:,} is {lesser:,}")


if __name__ == "__main__":
    # Calls the "main" function.
    main()
