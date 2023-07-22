#!/usr/bin/env python3
"""sum_multiples.py"""

# This code displays the sum of all natural numbers less than 1900 that are divisible
#  by both 7 and 11. Code is modified from that given by  Dr. David Biersach
#  in perfect_numbers.py.


def is_divisible_by_7(i: int) -> bool:
    """Determine if i is divisible by 7"""
    # i = range of numbers being summed defined as an integer.
    return i % 7 == 0


def is_divisible_by_11(i: int) -> bool:
    """Determine if i is divisible by 11"""
    # i = range of numbers being summed defined as an integer.
    return i % 11 == 0


def main() -> None:
    """Summation of numbers divisible by 7 and 11 between 1 and 1900"""
    # Initializing sum_divisible as an integer, first equal to 0
    sum_divisible: int = 0
    # Loop runs over a sequence of numbers for 1 to 1900 in increments of 1
    for n in range(1, 1901, 1):
        # Checks if the number is divisible by 7 and 11
        if is_divisible_by_7(n) and is_divisible_by_11(n):
            # Adds the number to sum_divisible
            sum_divisible += n
    # Prints sum_divisible with commas
    print(f"Sum of numbers divisible by 7 and 11 = {sum_divisible:,}")


if __name__ == "__main__":
    # Call the main function (which runs is_divisible_by_7 and is_divisible_by_11 above)
    main()
