#!/usr/bin/env python3
"""euler_curve.py"""

# This code plots a 2D parametric curve, displays the arc length, and plots the point at the limit 𝑡→∞.

# Code is aided by the following online resources:
# https://en.wikipedia.org/wiki/Euler_spiral#Expansion_of_Fresnel_integral
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.fresnel.html
# https://en.wikipedia.org/wiki/Fresnel_integral

# Used for type hinting
from __future__ import annotations

# Used for type hinting
import typing

# Used for plotting
import matplotlib.pyplot as plt

# Used for calculations
import numpy as np

# Calculate fresnel integrals
from scipy.special import fresnel  # type: ignore

if typing.TYPE_CHECKING:
    # allow type hints for axes and arrays
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def find_limit(t_large: float) -> tuple[float, float]:
    """Find the limit (x and y points) of the spiral as t approaches infinity"""
    # plug a very large t value into the fresnel operator and return the output
    S_large, C_large = fresnel(t_large)
    return S_large, C_large


def plot(ax: Axes) -> None:
    """Plot the given data set"""
    # create an array of t values
    t: NDArray[np.float_] = np.linspace(0, 12.34, 300)

    # Since the scipy fresnel function calculates integral (sin(pi/2(t^2)))->
    # we need to divide by pi/2 now so that the output is for integral (sin(t^2)) later
    t_adjusted = t / (np.pi / 2)
    # Define the sin and cos fresnel integrals
    S, C = fresnel(t_adjusted)
    # Define the x and y values based on the output of the fresnel integrals
    x: NDArray[np.float_] = C
    y: NDArray[np.float_] = S

    # Find the limit as t approaches infinity
    t_large = float = 1_000_000
    y_lim, x_lim = find_limit(t_large)

    # Plot the x and y values
    ax.plot(x, y)
    # Plot the limit as t approaches inf
    ax.scatter(x_lim, y_lim, color="red", label=r"$\lim_{t\to \infty}$")
    # Set labels using latex
    ax.set_xlabel(r"x=$\int(\cos(t^2))$")
    ax.set_ylabel(r"y=$\int(\sin(t^2))$")
    ax.legend()

    # Arc length L can be defined as integral(sqrt(dx^2+dy^2))=integral (dt)= t0 where
    # dx= cos(t^2)dt, dy=sin(t^2)dt
    arclength = t[-1]
    ax.set_title(f"Euler Curve with Arc Length= {arclength:0.05}")


def main() -> None:
    """Define an entry point for the script"""
    # Open up a new file window
    plt.figure(__file__)
    # Plot the function
    plot(plt.axes())
    # Show the plot
    plt.show()


if __name__ == "__main__":
    """Call the main function"""
    main()
