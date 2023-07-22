#!/usr/bin/env python3
"""factor_quadratic.py"""

# This code attempts to factor quadratic expressions.
# Code is modified from that given by Dr. David Biersach in factor_quadratic.py.


def factor_quadratic(h: int, i: int, j: int) -> None:
    """Displays factors of the quadratic polynomial Jx^2 + Kx + L"""
    print(f"Given the quadratic: {h}x^2 + {i}x + {j}")
    # Set up a boolean variable for factored or not factored
    # just to make sure the statement in line 36 will only be printed once.
    factored: bool = False

    # For h, we must try for every integer a where 1 ≤ 𝒂 ≤ h.
    for a in range(1, h + 1):
        # If there is no remainder
        if h % a == 0:
            # C is updated.
            c: int = h // a
            # For j, we must try for every integer b where 1 ≤ b ≤ j.
            for b in range(1, j + 1):
                # If there is no remainder
                if j % b == 0:
                    # d is updated
                    d: int = j // b
                    # If this is true (𝒂𝒅+𝒃𝒄)==i, the quadratic has been factored.
                    if int(a * d + b * c) == i:
                        print(f"The factors are: ({a}x + {b})({c}x + {d})")
                        factored = True  # factored boolean variable is reset to true.

    if not factored:
        # If not factored, print
        print(f"The expression {h}x^2 + {i}x + {j} cannot be factored")


def main() -> None:  # Defines an entry point for the code.
    # Calls factor_quadratic for the given variables.
    factor_quadratic(115425, 3254121, 379021)


if __name__ == "__main__":
    # Calls the main function
    main()
