#!/usr/bin/env python3
"""plot_trajectory.py"""

# EDITED-> Initially, I calculated the original height with the incorrect final height value.

# This code displays the path of a secondary particle given in the ray.csv file,
# and determines a line of best fit to find the particle's velocity and the height
# at which it was originally emitted in the stratosphere.

# Code is modified from that given by Dr. David Biersach in quadratic_regression_sklearn.py.
# Code is also aided by:
# https://scikit-learn.org/stable/modules/linear_model.html
# https://docs.scipy.org/doc/scipy/reference/constants.html

# If path errors arise, type-> cd "./Session 16 - Scientific Computing/" and
# then python ./plot_trajectory.py ./ray.csv first before running.


# Allows for annotations and type hints
from __future__ import annotations

# Allow for type hints
import typing

# Used for plotting
import matplotlib.pyplot as plt

# Used for calculations
import numpy as np

# Allow for minor ticks
from matplotlib.ticker import AutoMinorLocator

# Used for line of best fit
from sklearn.linear_model import LinearRegression

# Generates C -> speed of light
import scipy.constants as sc  # type:ignore

# For type checking
if typing.TYPE_CHECKING:
    # allows type hints for axes and arrays
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def fit_linear(ts: NDArray[np.float_], ys: NDArray[np.float_]) -> tuple[float, float]:
    # Make ts a 2d matrix
    ts = ts[:, np.newaxis]
    # Create a linear regression fit of ts vs ys
    model: LinearRegression = LinearRegression().fit(ts, ys)
    # Slope is the first coefficient value in model
    m: float = float(model.coef_[0])
    # b is the y intercept
    b: float = float(model.intercept_)  # type: ignore
    # Return the slope and y intercept as a tuple of floats
    return m, b


def projectile(
    m: float, ts: NDArray[np.float_], ys: NDArray[np.float_]
) -> tuple[float, float]:
    """Use kinematics equations to find the starting velocity and height of the projectile"""
    # Define Vy, m is given in cm/ns, convert to m/s
    # print (f"{m}")
    vy: float = m * (1 / 100) * ((1e9) / 1)
    # convert t from ns to s
    t: float = ts[-1] / (1e9)
    # Define the total time the particle lived in seconds
    total_t: float = 0.0001743
    # calculate t_start for the kinematics calculations
    t_start: float = total_t - t
    # Define gravitational acceleration
    g: float = 9.8  # m/s^2
    # Find V0y
    v0y: float = vy + (g * t_start)
    # Convert v0y to cm/ns for printed value
    convert_v0y: float = v0y * (100 / 1) * (1 / (1e9))
    # use scipy constants to find v0y relative to c
    relative_v0y: float = v0y / sc.speed_of_light
    print(f"Particle's initial velocity: {convert_v0y:.3f}in cm/ns")
    print(f"Particle velocity relative to c: {relative_v0y:.3f} in m/s")
    # Define y_final as the starting element of ys
    y: float = ys[-1]
    # Fine y0 in km using kinematics equation
    y0: float = -(((pow(v0y, 2) - pow(vy, 2)) / (2 * g)) - y)
    print(f"Initial height: {y0/1000:,.3f} in km")
    return relative_v0y, y0


def plot(ts: NDArray[np.float_], ys: NDArray[np.float_], ax: Axes) -> None:
    """Plot the sampled trajectory from ts and ys"""
    ax.set_title("Secondary Particle Trajectory")
    ax.set_xlabel("time (ns)", loc="right")
    ax.set_ylabel("Height (cm)")
    # Plot ts and ys using a scatter plot
    ax.scatter(ts, ys, color="red", label="Actual Data")
    min_x: float = float(np.min(ts))
    max_x: float = float(np.max(ts))
    # Define x as an array from the minimum to maximum time values
    x: NDArray[np.float_] = np.linspace(min_x, max_x, 1000)
    # Slope m is initialized to a float value
    m: float
    # call the fit_linear helper function to get slope and y-int
    m, b = fit_linear(ts, ys)
    # Plot the line of best fit
    ax.plot(x, m * x + b, label="Linear Fit")
    # use projectile helper function to get initial height and particle velocity
    projectile(m, ts, ys)
    # Use a legend
    ax.legend()
    # Use automatic tick marks
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())


def analyze(file_name: str) -> None:
    # we can generate a multidimensional array from a data file using np.genfromtxt
    samples: NDArray[np.float_] = np.genfromtxt(file_name, delimiter=",")
    # We know the array is 2d
    # So we should slice up the 2d matrix into two columns
    # since samples is a 2d array, so we only want the first column so use ,0
    ts: NDArray[np.float_] = samples[:, 0]
    # now we want the second column, use ,1
    ys: NDArray[np.float_] = samples[:, 1]
    # open up a plot window
    plt.close("all")
    # create a figure, constrained...-> minimize white space around the plot to get more
    # rendering on the screen
    plt.figure(file_name, constrained_layout=True)
    # Call the plot helper function
    plot(ts, ys, plt.axes())
    plt.show()


def main() -> None:
    """Define an entry point for the function"""
    analyze("ray.csv")


if __name__ == "__main__":
    """Call the main function"""
    main()
