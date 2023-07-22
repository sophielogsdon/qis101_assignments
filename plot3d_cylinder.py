#!/usr/bin/env python3
"""plot3d_cylinder"""

# This code uses matplotlib to draw a wireframe cylinder with a unit radius centered at (0, 0, 0).

# Code is modified from that given by Dr. David Biersach in plot3d_sphere.py

# Allows for type hints
from __future__ import annotations

# Allows for type hints
import typing

# Used for plotting
import matplotlib.pyplot as plt

# Used for calculations
import numpy as np

if typing.TYPE_CHECKING:
    # Type hint axes and arrays(for vectorized operations)
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def plot(ax: Axes) -> None:
    """Plot the cylinder"""
    # Theta values range from 0 to 2pi
    theta: NDArray[np.float_] = np.linspace(0, 2 * np.pi, 30)
    # Unit radius= 1
    r: float = 1.0
    # x=rcos(theta), y=rsin(theta)-> arrays to do vectorized operations
    x: NDArray[np.float_] = r * np.cos(theta)
    y: NDArray[np.float_] = r * np.sin(theta)
    # z=z
    # z is initialized to an array between 0 and 1 in 30 steps
    z: NDArray[np.float_] = np.linspace(0, 1, 30)
    # Use np.meshgrid to create a 2d grid between z and theta
    # Bumps z up to a 2d array so we can use the wire frame plotter
    theta_grid, z_grid = np.meshgrid(theta, z)
    # Boost z to a 2d array
    z = z_grid
    # Set the x,y, and z labels
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    # Matplotlib still doesn't recognize z type hint, so ignore
    ax.set_zlabel("z")  # type: ignore
    # Plot the cylinder using a wire frame
    ax.plot_wireframe(x, y, z_grid)  # type: ignore


def main() -> None:
    """Define an entry point for the function"""
    # create a figure, constrained...-> minimize white space around the plot to get more
    # rendering on the screen -> nice when we have 3 axes
    plt.figure(__file__, constrained_layout=True)
    # specify the projection to be 3d
    plot(plt.axes(projection="3d"))
    # show the plot
    plt.show()


if __name__ == "__main__":
    """Call the main function"""
    main()
