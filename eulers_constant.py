#!/usr/bin/env python3
"""eulers_constant.py """

# Edited: My initial attempt had an incorrect plot. 

# Code is aided by solutions provided by Dr. David Biersach. 

# This code uses SciPy to numerically estimate Euler's Constant:
#𝛾=−∫_0^1〖ln⁡ln⁡(1/𝑥)  ⅆ𝑥. Then uses pyplot to superimpose a line graph of 𝛾+ln⁡(𝑥) 
# on top of a step plot of the first 50 Harmonic Numbers.

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
    
# Import scipy's integration function
from scipy.integrate import quad # type: ignore


def eulers_constant_integrand (x: float) -> float:
    """Calculate the integrand for Euler's Constant"""
    # ln⁡ln⁡(1/𝑥) 
    return float (np.log(np.log(1/x)))


def eulers_constant(x: float) -> float:
    """Take the integral of the integrand to find Euler's Constant"""
    # 𝛾=−∫_0^1〖ln⁡ln⁡(1/𝑥)  ⅆ𝑥〗
    eulers_constant: float = -quad(eulers_constant_integrand, 0, 1)[0]
    return eulers_constant

def plot(ax: Axes) -> None:
    """Plot the functions as step plots"""
    # Initialize x to an array of floating values between 0 and 50 
    x: NDArray[np.float_] = np.linspace(0, 50, 500)
    # Get a list of the values for 𝛾+ln⁡(𝑥) using the helper functions above 
    # and a list comprehension
    plot_euler: list [np.float_]= [eulers_constant(value) + (np.log (value)) for value in x]
    # Calculate the first 50 Harmonic Numbers using a list comprehension
    harmonic_series_values: list [np.float_]= [np.sum(1/np.arange (1, value+1 ))for value in x]
    # Set the plot title
    ax.set_title("Asymptotic Limit of the Harmonic Numbers")
    # Set the x axis label
    ax.set_xlabel("X")
    # Set the y axis label
    ax.set_ylabel("Harmonic Number")
    # Set tick marks at intervals of 5 along the x axis
    ax.xaxis.set_major_locator(MultipleLocator(5))
    # Calculate the y_max to set the y_ticks because the x axis ticks 
    # and y axis ticks will not be equal
    y_max: np.float_ = np.float_(max(np.array((plot_euler)+(harmonic_series_values))))
    # Set the y axis ticks using y_max
    ax.yaxis.set_major_locator(MultipleLocator(base= float(y_max)/5))
    # Plot the harmonic numbers and eulers constant +ln(x)
    ax.plot(x, plot_euler, label=r"$\gamma$+ln(x)")
    ax.step (x, harmonic_series_values, label= "First 50 Harmonic Series Values")
    # Only plot positive y axis values
    ax.set_ylim (bottom=0)
    # Create a legend
    ax.legend()
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
