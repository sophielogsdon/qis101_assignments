#!/usr/bin/env python3
"""prime_racer4.py"""

# fmt: off

# This code decreases the runtime of the prime_racer3.py program 
# provided by Dr. David Biersach.

# Import the square root function.
from math import sqrt
# Import random integer and see functions. 
from random import randint, seed
# Import process time so we can generate an elapsed time for this program.
from time import process_time
 


def find_primes(min_p: int, max_p: int) -> list[int]:
    """Computes an array of primes between 2 and sqrt(1_000_000)"""
    # p is equal to an empty list with type integer. 
    p: list[int] = []
    
    for n in range(min_p, max_p):
        # Generator expression that checks if the remainder of n/factor 
            # does not equal zero between 2 and sqrt (n)+1
        if all(n % factor != 0 for factor in range(2, int(sqrt(n)) + 1)):
            # If the generator expression is true, add value n to list p
            p.append(n)    
    return p


def is_prime(n: int, p: list[int]) -> bool:
    """Returns True/False if the given number is prime"""
    # Generator expression that creates a series of boolean values to indicates 
    # whether n is divisible by an element of p 
    return all(n % factor != 0 for factor in p)
    


def main() -> None:
    # Identifying the seed value for the random number generator.
    seed(2016)
    # Number of samples set to 10_000
    num_samples: int = 10_000
    #Minimum value is set to 100_000
    min_val: int = 100_000
    # Maximum value is set to 1_000_000
    max_val: int = 1_000_000
    

    print(
        (
            f"Counting the number of primes in {num_samples:,} random samples\n"
            f"with each sample having a value between {min_val:,} "
            f"and {max_val:,} inclusive . . ."
        )
    )
    # List comprehension that generates a list of 10_000 random integers. 
    samples: list[int] = [randint(min_val, max_val) for _ in range(num_samples)]
    # Start time is set to the current value of the CPU time. 
    start_time: float = process_time()
    max_p: int = int(sqrt(max_val)) + 1
    # Call function find primes
    p: list[int] = find_primes(2, max_p)
    # Enumerate through the list and figure out which ones are prime. 
    # is_prime returns boolean true or false 
    num_primes: int = sum(is_prime(n, p) for n in samples)
    # Elapsed time is calculated from the current CPU time minus the start time.
    elapsed_time: float = process_time() - start_time
    # Print elapsed_time with floating point decimals to 3 places.
    print(f"Number of primes found: {num_primes:,}")
    print(f"Total run time (sec): {elapsed_time:.3f}\n")
    


if __name__ == "__main__":
    main()
