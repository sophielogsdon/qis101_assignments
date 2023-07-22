#!/usr/bin/env python3
"""ladder_problem.py"""


# This code uses SciPy to calculate and display the maximum ladder length possible 
# that will fit around the corner depicted in slides provided by Dr. David Biersach. 

# Code was aided by graphing visualization provided by:
# https://www.wolframalpha.com/widgets/gallery/view.jsp?id=c5e70574a3c9db7c84505985651757ac
# And the following online resources: 
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize_scalar.html#scipy-optimize-minimize-scalar
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.fsolve.html#scipy.optimize.fsolve
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.misc.derivative.html#scipy.misc.derivative
# Used for type hinting
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
# Used to find local extrema and derivative 
from scipy.optimize import minimize_scalar, fsolve # type: ignore
from scipy.misc import derivative # type: ignore


def length(C1: int, C2: int, theta: NDArray[np.float_]) -> list [float]:
    """Calculate the length of the ladder based on the equation 
    1/(sin(x)) + 2/(cos(x))"""
    # Initialize length_result as a list of floating points 
    length_result: list [float] = []
    # For each angle in the theta list 
    for value in theta:
        # Check that the solution to the length equation actually exists 
        # (there are several asymptotes)
        if np.sin(value) != 0 and np.cos(value) != 0 and value % (np.pi / 2) != 0:
            # Append that solution to the length_result list 
            length_result.append(C1 / np.sin(value) + C2 / np.cos(value))
        else:
            # Otherwise, it is not a number and this will be appended at that value in 
            # theta to account for the asymptotes
            length_result.append(np.nan)
    # Return the list 
    return length_result

def length_function(x:float)->float:
    """Define the length function separately from the graphed values in order to use scipy optimization functions more easily """
    # Return the function as a float
    return 2/np.sin(x) + 1/np.cos(x)

def d_length_function(x:float)-> float: 
    """Use scipy operators to calculate the derivative """
    # Probably should have used a more updated operator than derivative 
    return derivative (length_function,x,dx=1e-6)

def plot(ax: Axes,  zoom: bool) -> None:
    """Plot the length of the ladder as a function of theta"""
    # initialize the width's of the hallways
    C1: int = 2
    C2: int = 1
    # Initialize theta as an array from 0 to 2pi
    theta: NDArray[np.float_] = np.linspace(0, np.pi/2, 1000)[1:-2]
    # Calculate length result using the helper function 
    length_result: list [float] = length(C1, C2, theta)
    # Plot the result where asymptotes are in solid blue lines?
    plt.plot(theta, length_result, 'b-', marker='o', markerfacecolor='white', markersize=5)

    # Since graph is quite confusing with x and y limits, I arbitrarily chose these 
    # limits to make the graph more readable.
    if zoom:
        ax.set_ylim(bottom=0, top=100)
        ax.set_xlim(left=0, right=np.pi/2)

    # Find the extrema using scipy

    # Calculate the maximum result using scipy minimize_scalar functions, set boundaries 
    # between 0 and the domain limit (x!= k*pi/2)
    result: float = minimize_scalar(length_function, bounds=(0, np.pi/2), method='bounded')
    # Return the maximum x value
    x_max:float = result.x
    # Return the maximum L value
    L_max:float = result.fun
    # Print the maximum 
    print()
    print (f"The maximum length of the ladder is {L_max} at {x_max}")
    print()
    # Plot the maximum value as a dot slightly larger than the dot for dL/d(theta)=0
    plt.plot ([x_max], [L_max], "go", label= "Maximum Length", markersize=10)
    
    # Plot the points where dL/dtheta=0 

    # Call the helper derivative function and 
    # use scipy's fsolve operator to find the roots of the given function 
    zero: float = fsolve(d_length_function, np.pi/2)[0]
    # Get the length value at that zero 
    length_zero: float = length_function (zero)
    # Plot the 0 point and add a label on the legend
    plt.plot (zero, length_zero, "ro", label = r"dL/d($\theta$) =0")
    # Plot the legend
    plt.legend()
    # Plot grid lines
    plt.grid(True)
    # Set the title 
    ax.set_title(f"Maximum Ladder Around a Corner: {L_max}")
    # Set the x axis label using latex
    plt.rcParams["text.usetex"] = True
    ax.set_xlabel(r"$\theta$ (radians)")
    # Set the y axis label 
    ax.set_ylabel("Length (m)")
    # Set major ticks along the x axis 
    ax.xaxis.set_major_locator(MultipleLocator(1))



def main(zoom: bool = True)-> None:
   """Define an entry point for the function"""
   # Create a new figure and set its name to the current code's filename
   plt.figure (__file__)
   # Call the plot function and pass through plt.axes()
   plot (plt.axes(), zoom)
   # Show the plot
   plt.show()
if __name__== "__main__":
   # Call the main function
   main()
