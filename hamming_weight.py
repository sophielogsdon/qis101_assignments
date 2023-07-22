#!/usr/bin/env python3
"""hamming_weight.py"""

# fmt: off


# This code implements a function to calculate the population count of a given integer. 
# It then compares the result of my function to that of a pre-existing one in python. 
# Code is modified from that of Dr. David Biersach in list_cards.py and dealer_slow.py. 
# Code is aided by online resources linked directly below: 
# https://stackoverflow.com/questions/15233121/calculating-hamming-weight-in-o1
# https://indepth.dev/posts/1019/the-simple-math-behind-decimal-binary-conversion-algorithms#:~:text=To%20convert%20integer%20to%20binary,remainders%20in%20the%20reverse%20order.
# https://www.geeksforgeeks.org/declare-an-empty-list-in-python/ to find code)
# https://en.wikipedia.org/wiki/Hamming_weight#:~:text=In%20error%2Dcorrecting%20coding%2C%20the,has%20a%20weight%20of%204.
# https://www.youtube.com/watch?v=5Km3utixwZs 
# https://www.w3schools.com/python/python_lists_add.asp
# https://note.nkmk.me/en/python-int-bit-count/ 

# Import the random integer function from the random library.
from random import randint 


def convert_to_binary (number: int) -> list[int]:
    """Define a function that will convert a given integer into a list corresponding to its binary values."""
    # Sets binary equal to an empty list
    binary: list[int] = []
    # To convert an integer into binary: divide the integer by 2 and store the remainders of 1 or 0 in a list. 
    # Repeat until you get a quotient of 0. 
    # Then reverse the order of the list
    while number > 0:
        remainder: int = number % 2
        if remainder == 1 or remainder == 0:
            binary.append(remainder)
        number = number // 2
    binary.reverse ()
    return binary
   



def hamming_weight (binary:list[int]) -> int: 
    """Defines the function that will manually calculate the population count of an integer."""
    # Create a boolean list equal to the length of binary to ensure that each index in binary is only checked once
    already_counted: list[bool] = [False] * len(binary)
    result: int = 0
    # For every binary position in a range the length of the binary list:
    for binary_pos in range(len(binary)): 
        # Updated binary position is randomly generated between 0 and (1- length of binary) (because the first index is 0)
        new_binary_pos: int = randint(0, len(binary)-1)
        #Runs until a new binary position is found
        while already_counted[new_binary_pos]: 
            # New binary position is recalculated
            new_binary_pos = randint(0, len(binary)-1)
        # If the value at binary_pos equals 1, update the hamming weight.
        if binary [binary_pos] == 1: 
           result +=1
        # Basically now this function checks whether or not an index of binary has been 
        # counted. If it has it picks a new random index to check for 1's until all have been checked. 
        already_counted[new_binary_pos] = True
        
    return result

def check_hamming_weight(number: int) -> int:
    """Counts the number of 1 bits in an integer. """
    return bin(number).count('1')

def main() -> None:
    number: int = 95_601
    # binary is defined as an integer list equal to the result of the conversion function
    binary:list [int] = convert_to_binary(number)
    result:int = hamming_weight(binary)
    check_hamming: int = check_hamming_weight(number)
    print(f"The Hamming weight of {number} is: {result}")
    print(f"Using Python's bit_count(), the hamming weight is: {check_hamming}")

if __name__ == "__main__":
    main()
