#!/usr/bin/env python3
"""board_encoding.py"""

# This code can decode a given integer representation of a 
# specific configuration of a Tic-Tac-Toe board. 
# For a board square, a zero (0) indicates the square is open, 
# a 1 represents an X and a 2 represents an O



def convert_to_ternary (number: int) -> list[int]:
    """Define a function that will convert a given integer into a list corresponding 
    to its ternary values."""

    # Sets ternary equal to an empty list 
    ternary: list[int] = []
    
    # To convert an integer into ternary: divide the integer by 3 and store 
    # the remainders of 2, 1, or 0 in a list. 
    # Repeat until you get a quotient of 0 and/or 
    # a list with length = 9 (length of a Tic-Tac-Toe board). 
    # No need to reverse the order, since that is already part of the encoding scheme. 
    while number > 0:
        remainder: int = number % 3
        if remainder == 1 or remainder == 0 or remainder==2:
            ternary.append(remainder)
        number = number // 3
    while len(ternary)<9: 
        if number ==0: 
            ternary.append(number)
    # Returns the conversion
    return ternary


def main() -> None: 
    # Defines an entry point for the function 

    number: int = 2271
    
    # ternary is defined as an integer list equal to the result of the conversion function
    ternary:list [int] = convert_to_ternary(number)
    

    print(f"The ternary version of {number} is: {ternary}")
    # Print the ternary list like a tic-tac-toe board
    print (f"{ternary [0], ternary [1], ternary [2]}\n{ternary [3], ternary [4], ternary [5]}\n{ternary [6], ternary [7], ternary [8]}")
    # Print a space in between each board
    print ()

    number= 1638
    
    ternary = convert_to_ternary(number)
    
    print(f"The ternary version of {number} is: {ternary}")
    print (f"{ternary [0], ternary [1], ternary [2]}\n{ternary [3], ternary [4], ternary [5]}\n{ternary [6], ternary [7], ternary [8]}")
    print ()

    number= 12065
    # ternary is defined as an integer list equal to the result of the conversion function
    ternary = convert_to_ternary(number)
    
    print(f"The ternary version of {number} is: {ternary}")
    print (f"{ternary [0], ternary [1], ternary [2]}\n{ternary [3], ternary [4], ternary [5]}\n{ternary [6], ternary [7], ternary [8]}")
    print ()
   

if __name__ == "__main__":
    # Calls the main function 
    main()
    