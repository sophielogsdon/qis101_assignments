#!/usr/bin/env python3
"""random_walk_gamma.py"""

# This code plots the expected final distance of a uniform random walk on a unit
# lattice having dimensions 1 to 25.
# Code is modified from that given by Dr. David Biersach in random_walk_lattice.py
# Code is also aided by the following online resources:
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.gamma.html
# https://www.math.uchicago.edu/~lawler/reu1
# https://en.wikipedia.org/wiki/Euler%27s_constant


# Annotations can be evaluated as expressions not comments.
from __future__ import annotations

# Import the typing module to add certain type hints
import typing

# Import the matplot library for graphing later on
import matplotlib.pyplot as plt

# Import numpy
import numpy as np

# use type: ignores for scipy because that module doesn't have type hints
# Import euler's gamma to be used in calculations
from scipy.special import gamma  # type: ignore

if typing.TYPE_CHECKING:
    # Import the ax.plotting functions
    from matplotlib.axes import Axes

    # Allows us to do verctorized operations
    from numpy.typing import NDArray


def expected_distance(dims: float) -> float:
    """expected_distance is defined as a floating point value based on the
    number of dimensions"""
    # Calculates the expected (mean) value of the final distance from
    # the origin for dimension d using gamma
    # Defined as a floating point
    expected_mean: float = 2 / dims * (gamma((dims + 1) / 2) / gamma(dims / 2)) ** 2
    return expected_mean


def main() -> None:
    """Defines an entry point for the function"""
    # Defines the initial number of dimensions
    starting_dim: int = 1

    # Defines the final number of dimensions
    stopping_dim: int = 25

    # Dimension is an array of floating point values made up of a linspace list that
    # starts at the initial dimension and ends at the final dimension, split into
    # 25 increments.
    dimensions: NDArray[np.float_] = np.linspace(starting_dim, stopping_dim, 100)

    # List comprehension that runs over each value of dimensions and calls the expected_
    # distance function for each dims element
    expected_distances: list[float] = [expected_distance(dims) for dims in dimensions]

    # Sets the figure name equal to the file size, and sets the figure size
    plt.figure(__file__)

    # Plots the axes
    ax: Axes = plt.subplot(111)

    # Plot a graph of dimensions vs expected_distances
    ax.plot(dimensions, expected_distances)

    # Write the title using latex
    ax.set_title(
        f" Tested Uniform Random Walk on {dimensions [0]} to {dimensions [-1]}-D Unit Lattice"
    )

    # Plot the graph in green
    ax.plot(dimensions, expected_distances, color="green")

    # X axis is the number of dimensions
    ax.set_xlabel("Number of Dimensions")

    # Y axis is the mean final distance
    ax.set_ylabel(r"$(Mean\;Final\;Distance)$")

    # Plot the graph
    ax.plot()

    # Show the graph
    plt.show()


if __name__ == "__main__":
    """Call the main function"""
    main()
