#!/usr/bin/env python3
"""benfords_law.py"""

# This code demonstrates the Law of Anomalous Numbers by calculating the 
# probability of each digit (1 to 9) appearing as the most significant digit (far left) 
# in 100,000 very large random numbers. 
# Code is copied and annotated from that given by Dr. David Biersach. 
# Code documentation for z_order was aided by: https://matplotlib.org/stable/gallery/misc/zorder_demo.html


# Allows for annotations for variables and return types
from __future__ import annotations
# Imports the typing module to aid with type hints
import typing
# Provides functions for creating plots
import matplotlib.pyplot as plt
# Sets ticks on the plot axes
from matplotlib.ticker import MultipleLocator 
# Import allows us to use arrays (so we can perform calculations on lists of numbers)
import numpy as np 
# Used for generating random numbers
import random 
# if the script is type checking
if typing.TYPE_CHECKING: 
    # Allows us to use Axes as a variable type
    from matplotlib.axes import Axes 
    # Allows us to use arrays
    from numpy.typing import NDArray 

def p_MSD()->NDArray[np.float_]:
    """Calculate the most significant digit in accordance with Benford's Law"""
    # p= array of probabilities 
    # p is initialized to an array of zeros, 
    # eventually we will store the count of each MSD
    p: NDArray[np.float_]= np.zeros (10, dtype=np.float_)
    # 100,000 very large random numbers
    # _ because we don't care what the actual number is
    for _ in range (100_000):
        # random integer
        # chosen from a uniform distribution 
        # between 1 and 1,000,000 (inclusive, inclusive)
        # and then raised to the 100th power
        n: int = random.randint (1,1_000_000)**100
        # Convert the random number n to a string
        # Get the element at the first index in the string(MSD)retrieved as a character 
        # Convert the element back into an integer 
        # Increase the count in p that corresponds to that integer
        p[int(str(n)[0])]+=1
    # Remove first element of p because Benford's Law does not include 0
    p = p[1:]
    # Get the probability of each element occurring by dividing by the 
    # total amount of large numbers
    p = p/100_000
    # MSD returns p array 
    return p 

def plot (ax:Axes)-> None: 
    """Plot the histogram"""
    # Create a bar plot 
    # Digits occur between 1 and 9 
    # zorder=2.5 allows higher bars to appear on top of lower value bars 
        # Essentially the order the bars appear in 
    plt.bar(range(1,10), p_MSD(), zorder=2.5)
    # Plot with grid lines
    plt.grid()
    # Set the plot title
    ax.set_title ("Benford's Law")
    # Set the x label
    ax.set_xlabel ("Most Significant Digit (MSD)")
    # Set the y label
    ax.set_ylabel ("Probability of MSD")
    # Major ticks are placed in intervals of 1
    ax.xaxis.set_major_locator (MultipleLocator(1))

def main()-> None: 
    """Define an entry point for the function"""
    # Create a new figure and set its name to the current code's filename
    plt.figure (__file__)
    # Call the plot function and pass through plt.axes()
    plot (plt.axes())
    # Show the plot
    plt.show()
if __name__== "__main__": 
    # Call the main function
    main()