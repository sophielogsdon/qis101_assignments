#!/usr/bin/env python3
"""plot3d_complex_sine.py"""

# This code uses matplotlib to draw the surface in ℂ given by 𝑓(𝑧)=|sin⁡(𝑧) | over the region (±2.5±𝑖)

# Code is modified from that given by Dr. David Biersach in plot3d_surface.py and complex_numbers.ipynb.

# Allows for type hinting
from __future__ import annotations

# Type hinting
import typing

# Used for plotting
import matplotlib.pyplot as plt

# Used for calculations
import numpy as np

# Use color maps
from matplotlib import cm

# Manually define how many tick marks we want
from matplotlib.ticker import LinearLocator

if typing.TYPE_CHECKING:
    # Allows for the type hint any, axes, and NDArray
    from typing import Any
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def f(z: NDArray[np.complex128]) -> NDArray[np.float_]:
    """abs(sin(z))"""
    # taking the sin of complex values and returning an array of floats
    return np.array(abs(np.sin(z)))


def plot(ax: Axes) -> None:
    """Plot abs(sin(z))"""
    # Real component of z occurs between +/-2.5
    real_z: NDArray[np.float_] = np.linspace(-2.5, 2.5, 100)
    # Imaginary component between +/-1 (for now)
    imag_z: NDArray[np.float_] = np.linspace(-1, 1, 100)
    # plot real_z and imag_z with a meshgrid-> essentially doing the outer product
    real_z, imag_z = np.meshgrid(real_z, imag_z)
    # Complex z is the sum of the real and imaginary components
    # (the imaginary component is multiplied by 1j here)
    complex_z: NDArray[np.complex128] = real_z + imag_z * 1j
    # Result is an array of floats from the helper function f
    result: NDArray[np.float_] = f(complex_z)

    # cmap= color map, does facet shading
    # (color for each facet has a palette correlated to the z value)
    surf: Any = ax.plot_surface(  # type: ignore
        real_z, imag_z, np.abs(result), cmap=cm.coolwarm, linewidth=0, antialiased=False  # type: ignore
    )
    ax.set_title("Complex Sine")
    # Set the x,y, and z labels
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    # Matplotlib still doesn't recognize z type hint, so ignore
    ax.set_zlabel("z")  # type: ignore
    # linear locator-> gives us exactly 10 tick marks
    ax.zaxis.set_major_locator(LinearLocator(10))  # type: ignore
    # can give it an f string to tell python how you want to format it
    ax.zaxis.set_major_formatter("{x:.02f}")  # type: ignore
    # Format the color bar
    plt.colorbar(surf, ax=ax, shrink=0.5, aspect=5)


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
