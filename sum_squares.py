#!/usr/bin/env python3
"""sum_squares.py"""

# This code sums the first 1000 natural numbers squared and compares the result with
#   that of the Gaussian summation. Code is modified from that given by
#   Dr. David Biersach in basel_series.py and perfect_numbers.py.


def sigma(n: int) -> float:
    """Summation for the squares of a given range of numbers defined later on"""
    # Define summation function as sigma (equal to float variable type
    # to allow for decimals).
    # n = range of numbers being summed defined as an integer.
    # Sum is defined as a float variable type, initialized at 0.0
    s: float = 0.0
    # For loop runs for a range from 1 to n with k=1,2,3...
    for k in range(1, n + 1):
        # Loop updates sum so that sum equals k squared.
        s += k**2
    # The function sigma should return s when it is called.
    return s


def main() -> None:  # Defining the entry point for the program.
    # Loop runs over a sequence of numbers for 1 to 1000 in increments of 1
    for num_terms in range(0, 1001, 1):
        # Variable series_sum is defined as a float type, set equal to the sigma,
        #   will run for num_terms.
        series_sum: float = sigma(num_terms)
    # Prints the solution of sigma with commas as thousands separators.
    print(f"Sum of first 1000 natural numbers squared {series_sum: ,}")


if __name__ == "__main__":
    # Call the main function (which runs sigma (num_terms) above)
    main()


def gaussian_sigma(n: int) -> float:
    """Gaussian summation"""
    # Define gaussian summation function (equal to float variable type
    # to allow for decimals).
    # n = range of numbers being summed defined as an integer.
    # Sum is a float type, equal to the formula for Gaussian sum
    s: float = ((2 * (n**3)) + (3 * (n**2)) + n) / 6
    # The function gaussian_sigma should return s when it is called.
    return s


def gaussian() -> None:  # Defines another entry point for the function
    # Loop runs over a sequence of numbers for 1 to 1000 in increments of 1
    for num_terms in range(0, 1001, 1):
        # Variable gaussian_sum is defined as a float type, set equal to the
        # gaussian_sigma, will run for num_terms.
        gaussian_sum: float = gaussian_sigma(num_terms)
    # Prints the solution of gaussian_sigma with commas as thousands separators.
    print(f"Sum  with the Gaussian method {gaussian_sum: ,}")


if __name__ == "__main__":
    # Call the gaussian function (which runs gaussian_sigma (num_terms) above)
    gaussian()
