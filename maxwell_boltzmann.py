#!/usr/bin/env python3
"""maxwell_boltzmann.py"""

# This code calculates and plots the probability density function (PDF) of 
# the Maxwell-Boltzmann distribution.
# Code is modified from that given by Dr. David Biersach in binomial_distribution.py 
# and freq_histogram.py.
# Code is also aided by the following online resources: 
# https://en.wikipedia.org/wiki/Maxwell–Boltzmann_distribution
# https://en.wikipedia.org/wiki/Thermodynamic_temperature
# https://en.wikipedia.org/wiki/Boltzmann_constant 
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.maxwell.html#scipy.stats.maxwell

# Allows for annotations for variables and return types
from __future__ import annotations

# To import Axes for plotting later and arrays for calculations
import typing
if typing.TYPE_CHECKING:
   from matplotlib.axes import Axes
   from numpy.typing import NDArray

# Used in calculations with arrays later on 
import numpy as np

# Helps plot the functions
import matplotlib.pyplot as plt

# Used to generate major tick marks on the plot
from matplotlib.ticker import MultipleLocator

# Scipy has a built-in Maxwell-Boltzmann distribution function
from scipy.stats import maxwell # type: ignore

def maxwell_boltzmann(ax: Axes) -> None:
   """Calculate the Maxwell Boltzmann distribution for the given a values and 
   plot the probability density"""

   # Limit the plot domain to 0≤𝑥≤20
   x_values: NDArray[np.float64] = np.linspace(0, 20, 500)

    # Calculate the PDF for the Maxwell Boltzmann distribution for a given a value
   dens1: NDArray[np.float64] =np.asarray( maxwell.pdf(x_values, scale=1))
   dens2: NDArray[np.float64] =np.asarray(maxwell.pdf(x_values, scale=2))
   dens3: NDArray[np.float64] = np.asarray(maxwell.pdf(x_values, scale=5))

    #Super impose the PDF's on the same plot and label which a value they represent
   plt.plot(x_values, dens1, label="a = 1")
   plt.plot(x_values, dens2, label="a = 2")
   plt.plot(x_values, dens3, label="a = 5")

    # Set the title
   ax.set_title("Maxwell Boltzmann Distribution")
   # Set the x axis label (between 0 and 20)
   ax.set_xlabel("X")
   # Set the y axis label
   ax.set_ylabel("P(x)")
   # Set the location of the legend
   ax.legend(loc="upper right")
   # Set major ticks 
   ax.xaxis.set_major_locator(MultipleLocator(5))

def main() -> None:
   """Defines an entry point for the function"""
   # Associate the figure with the current script file to help manage multiple plots
   plt.figure(__file__)
   # Call the Maxwell helper function 
   maxwell_boltzmann(plt.axes())
   # Show the plot
   plt.show()

if __name__ == "__main__":
   # Call the main function
   main()

