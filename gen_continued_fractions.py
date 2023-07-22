#!/usr/bin/env python3
"""gen_continued_fractions.py"""

# This code finds the digits of pi using two GCF's found by Dr. David Biersach 
# and one found by Euler. 
# Code is copied from Dr. David Biersach 

# Import the math module for later calculations
import math

# Maximum number of terms in the continued fraction
MAX_TERMS: int = 20



def decode_gencf(form: tuple[int, ...]) -> float:
    """Evaluates a generalized continued fraction of the given form"""

    # Unpacking elements of the form tuple into individual variables.
    a0, b0, Ai, Bi, Ci, Di, Ei = form
    
    # Initialize an and bn
    an, bn = a0, b0
    
    # Initialize hn and kn
    hn, kn = 0.0, 0.0
    
    # Initialize b_1, h_1, and k_1
    b_1, h_1, k_1 = 1.0, 1.0, 0.0
    
    # Initialize h_2 and k_2
    h_2, k_2 = 0.0, 1.0
    
    # Loop runs for range of 1 to the max terms in the continued fraction
    for n in range(1, MAX_TERMS):
        # Decoding the continued fraction 

        #  ℎ_𝑛=𝑎_𝑛 ℎ_((𝑛−1) )+𝑏_((𝑛−1) ) ℎ_((𝑛−2) )
        hn = an * h_1 + b_1 * h_2

        #  𝑘_𝑛=𝑎_𝑛 𝑘_((𝑛−1) )+𝑏_((𝑛−1) ) 𝑘_((𝑛−2) )
        kn = an * k_1 + b_1 * k_2
        
        # Update value of b_1 to bn for the next run through the loop. 
        b_1 = bn

        # Update values of h_1 and h_2
        h_1, h_2 = hn, h_1

        # Update values of k_1 and k_2
        k_1, k_2 = kn, k_1

        # Update values of an and bn using this formula 
        #  𝑏_𝑛/𝑎_𝑛 =((𝐴_𝑖 ) 𝑛^2+(𝐵_𝑖 )𝑛+(𝐶_𝑖 ))/((𝐷_𝑖 )𝑛+(𝐸_𝑖 ) )
        an = Di * n + Ei
        bn = Ai * n * n + Bi * n + Ci
        # Calculate bn and an where 
        
    # As the code runs, we get a better approximation of (h/k) 
        # # to the original number of x
    return hn / kn



def print_rel_error(estimated: float, actual: float) -> None:
    """Printing the estimated, actual, and % error values for the GCF's for Pi"""

    # Print the estimated value
    print(f"Est.        : {estimated}")

    # Print the actual value
    print(f"Act.        : {actual}")

    # Calculate the percent error and print
    print(f"Rel. % Err  : {(actual - estimated)/actual:.14%}\n")


# Defines an entry point for the function
def main() -> None:
    """Finding the digits of pi using these continued fractions"""

    # 𝝅 = [a0; b0, {(bn)^2|an}]

    # Calculate the digits of Pi using Euler's GCF
    print("Euler's Generalized Continued Fraction for Pi")
    # Decode Euler's GCF
    x: float = decode_gencf((3, 1, 4, 4, 1, 0, 6))
    # Calculates error between x and pi
    print_rel_error(x, math.pi)

    # Calculate the digits of Pi using Biersach's first GCF
    print("Biersach's Generalized Continued Fraction #1 for Pi")
    # Decode Biersach's 1st GCF
    x = decode_gencf((3, 1, 8, 0, -7, 8, -1))
    # Calculates error between x and pi
    print_rel_error(x, math.pi)

    # Calculate the digits of Pi Using Biersach's second GCF
    print("Biersach's Generalized Continued Fraction #2 for Pi")
    # Decode Biersach's 2nd GCF
    x = decode_gencf((2, 8, 4, 8, 0, 4, 2))
    # Calculate error between x and pi
    print_rel_error(x, math.pi)

if __name__ == "__main__":
    main()
    # Call the main function 
