#!/usr/bin/env python3
"""werner_formula.py"""

# This code uses pyplot to plot four functions on one graph over the domain −3𝜋≤𝑥≤3𝜋. 
# Then, it uses LaTeX encoding to populate the legend labels for each curve. 

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

def f_1(a:NDArray [np.float_])->  NDArray [np.float_]: 
    """ f_1 (x)= sin (0.8x)"""
    # a is already defined as 0.8x 
    # Returns an array of float values 
    return (np.sin(a))

def f_2 (b: NDArray [np.float_])-> NDArray [np.float_]: 
    """f_2(x)= sin(0.5x)"""
    # b is already defined as 0.5x 
    # Returns an array of float values 
    return (np.sin (b))

def f_3 (f_1_values:NDArray [np.float_], f_2_values: NDArray [np.float_])-> NDArray [np.float_]: 
    """f_1 *f_2"""
    # Returns an array of floats 
    return (f_1_values *f_2_values)

def werner (a: NDArray [np.float_], b: NDArray [np.float_])-> NDArray [np.float_]:
    """Werner's product to sum formula for sin(alpha)*sin(beta)"""
        # -> 2sin(a)sin(b)= cos(a-b) +cos (a+b) -> sin(a)+sin(b)= (cos(a-b) +cos (a+b))/2
    return ((np.cos(a-b))-(np.cos(a+b)))/2

def plot (ax:Axes)-> None: 
    """Plot f1-f4 functions"""
    # X goes from -3pi-3pi in steps of 100
    x: NDArray [np.float_]= np.linspace (-3*np.pi, 3*np.pi, 100)
    # a= alpha=0.8x
    a: NDArray [np.float_]= 0.8*x
    # b=beta=0.5x
    b: NDArray [np.float_]= 0.5 *x
    # Call the helper functions for f_1 through f_4
    f_1_values: NDArray [np.float_]= f_1(a)
    f_2_values: NDArray [np.float_]= f_2(b)
    f_3_values: NDArray [np.float_]= f_3(f_1_values, f_2_values)
    f_4_values: NDArray [np.float_]= werner (a,b)
    # Set the title of the plot using latex 
    ax.set_title(f"Werner's Product to Sum Formula for: " rf"$2sin(\alpha)sin(\beta)$")
    # Plot f1 through f4 values as defined above, and create their legend labels using latex
    ax.plot(x, f_1_values, label=rf"$f_1=\sin⁡(0.8𝑥)$")
    ax.plot(x, f_2_values, label=rf"$f_2=\sin⁡(0.5𝑥)$")
    # Plot the dotted line of f_4 first and then f_3 to be able to see f_3 
    # Use linestyle= "--"to create dashed lines in between the white dots for f_4_values 
    ax.plot(x, f_4_values, marker='o', markerfacecolor='white', markersize=3, linestyle = "--", label=f"Werner's product to sum formula for: " rf"$(f_1(x)) \cdot (f_2(x))$")
    ax.plot(x, f_3_values, label=rf"$f_3=(f_1(x)) \cdot(f_2(x))$")
    # Set x label to x
    ax.set_xlabel("X")
    # Set y label to y 
    ax.set_ylabel("Y")
    # Create grid lines
    ax.grid()
    # Create a legend using the labels for f_1 through f_4 defined above 
    ax.legend()
    # Set tick marks at intervals of 5 along the x axis
    ax.xaxis.set_major_locator(MultipleLocator(5))
    # Set tick marks at intervals of 5 along the y axis 
    ax.yaxis.set_major_locator(MultipleLocator(5))
    # Set the axes to be equal
    ax.axis("equal")
    # Show the plot
    plt.show()

def main() -> None:
    """Defines an entry point for the function"""
    # Create a new figure and set its name to the current code's filename
    plt.figure(__file__)
    # Call the plot function and pass through plt.axes()
    plot(plt.axes())

if __name__ == "__main__":
    # Calls the main function 
    main()




