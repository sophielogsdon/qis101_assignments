#!/usr/bin/env python3
"""archimedes_spiral.py """

# Edited -> In my initial attempt, the arc length was calculated incorrectly, 
# the print statement for arc_length had incorrect syntax, 
# and the plot title did not correctly display.

# This code uses SciPy to calculate and display the arc length of an 
# Archimedes Spiral with 𝑟=𝜃 as it rotates from 0≤𝜃≤8𝜋 

# Code is modified from that given by Dr. David Biersach in stdnormal_area.py, 
# and aided by solutions given by Dr. Biersach.

# Code is aided by the following online resources: 
# https://mathworld.wolfram.com/ArchimedesSpiral.html
# https://en.wikipedia.org/wiki/Archimedean_spiral
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.quad.html#scipy.integrate.quad 
# https://math.stackexchange.com/questions/1650702/arc-length-of-archimedes-spiral-r-theta-from-0-le-theta-le-2-pi
# https://stackoverflow.com/questions/5965583/use-scipy-integrate-quad-to-integrate-complex-numbers

# Allows for annotations for variables and return types
from __future__ import annotations
# Imports the typing module to aid with type hints
import typing
# Provides functions for creating plots
import matplotlib.pyplot as plt
# Import allows us to use arrays (so we can perform calculations on lists of numbers)
import numpy as np
# Sets ticks on the plot axes
from matplotlib.ticker import MultipleLocator
# if the script is type checking
if typing.TYPE_CHECKING:
    # Allows us to use Axes as a variable type
    from matplotlib.axes import Axes
    # Allows us to use arrays
    from numpy.typing import NDArray
    
# Import scipy's integration function to calculate arc length 
# But the quad function seems to struggle with complex integration 
# So I will simplify the integral for it first using u substitution
from scipy.integrate import quad # type: ignore

def archimedes_spiral(u: float) -> tuple[NDArray[np.float_], NDArray [np.float_]]:
    """Define the equation for the archimedes spiral (r=theta)"""
    # U corresponds to theta 
    # Returns the values of x and y for the given u/theta value 
    # Returned as a tuple 
    return u * np.cos(u), u * np.sin(u)


def arc_length_integrand(u: float) -> float:
    """Define the integrand for calculating arc length first before using quad"""
    return float (np.sqrt(u**2+1))


def plot(ax: Axes) -> None:
    "Plot the archimedes spiral"
    # Generate a list of values for u (or theta) from 0 to 8pi in 1000 steps
    u: NDArray[np.float_] = np.linspace(0, 8 * np.pi, 1000)
    # Arc_length if equal to the integral of its integrand defined above
    arc_length: float = quad(arc_length_integrand, 0, 8 * np.pi)[0]
    # X is an array of the elements in the first index of the 
    # tuple returned by archimedes_spiral based on u
    x: NDArray[np.float_]= archimedes_spiral(u)[0]
    # y is an array of the elements in the second index of the 
    # tuple returned by archimedes_spiral based on u
    y: NDArray [np.float_]= archimedes_spiral (u)[1]
   # Set the title of the plot
    ax.set_title(f"Archimedes Spiral with arc length = {arc_length:.4f}")
    # Set the x axis label
    ax.set_xlabel("X")
    # Set the y axis label
    ax.set_ylabel("Y")
    # Set tick marks at intervals of 5 along the x axis
    ax.xaxis.set_major_locator(MultipleLocator(5))
    # Set tick marks at intervals of 5 along the y axis 
    ax.yaxis.set_major_locator(MultipleLocator(5))
    # Plot the spiral
    ax.plot(x, y)
    # Set the axes to be equal
    ax.axis("equal")
    # Show the plot
    plt.show()
    # Print the value of the arc length in the terminal 
    print(f"Arc Length:{arc_length:.4f}")

def main() -> None:
    """Defines an entry point for the function"""
    # Create a new figure and set its name to the current code's filename
    plt.figure(__file__)
    # Call the plot function and pass through plt.axes()
    plot(plt.axes())

if __name__ == "__main__":
    # Calls the main function 
    main()






