#!/usr/bin/env python3
"""plot_ellipse.py"""

# This code makes a 2D plot of an ellipse with a major axis of 100
# and a minor axis of 50.
# Code is modified from that given by Dr. David Biersach in plot_circle.py.
# Code is also aided by https://en.wikipedia.org/wiki/Ellipse.

# Annotations can be evaluated as expressions not comments.
from __future__ import annotations

# Import the typing module to add certain type hints
import typing

# Import the matplot library for graphing later on
import matplotlib.pyplot as plt

# Import numpy
import numpy as np


if typing.TYPE_CHECKING:
    # Import the ax.plotting functions
    from matplotlib.axes import Axes

    # Allows us to do verctorized operations
    from numpy.typing import NDArray


def plot(ax: Axes) -> None:
    """Calculates the ellipse in polar coordinates"""
    # Theta is an array of floating points between 0 and 2pi.
    # Ellipse is subdivided into 1000 equally spaced intervals to make the graph smooth.
    theta: NDArray[np.float_] = np.linspace(0, 2 * np.pi, 1000)

    # Major axis is defined to be 100
    major_axis: int = 100

    # Minor axis defined to be 50
    minor_axis: int = 50

    # Radius is an array calculated based on theta.
    # r =ab/ sqrt (a^2sin^2(theta)+b^2(cos^2(theta))) where a= major axis and b= minor axis
    radius: NDArray[np.float_] = (major_axis * minor_axis) / (
        (
            ((major_axis**2) * ((np.sin(theta)) ** 2))
            + ((minor_axis**2) * (np.cos(theta) ** 2))
        )
        ** (1 / 2)
    )

    # Polar to Cartesian coordinate conversion using vectorized operations

    # Passes theta array into cos and sin functions (vector aware)
    # Will automatically check each element in the array
    x: NDArray[np.float_] = radius * np.cos(theta)

    y: NDArray[np.float_] = radius * np.sin(theta)

    # Create a plot of x and y in the color red.
    ax.plot(x, y, color="red")

    # Create the title of the plot using latex (carrot symbols turn into exponents)
    ax.set_title(
        rf"$\frac{{x^2}}{{{major_axis}}}\;+\;\frac{{y^2}}{{{minor_axis}}} = 1$"
    )

    # Set the x axis label equal to x.
    ax.set_xlabel("x")

    # Set the y axis label equal to y
    ax.set_ylabel("y")

    # Creates grid lines
    ax.grid()

    # x=0 is drawn in black
    ax.axhline(0, color="black")

    # y=0 is drawn in black
    ax.axvline(0, color="black")

    # Correcting for the imperfection in the CPU pixel aspect ratio
    ax.set_aspect("equal")


def main() -> None:
    """Defines an entry point for the function"""
    # Sets the name of the figure equal to the file name
    plt.figure(__file__)

    # Plots the axes
    plot(plt.axes())

    # Shows the plot we just created
    plt.show()


if __name__ == "__main__":
    """Calls the main function"""
    main()
