#!/usr/bin/env python3
"""identify_element.py"""

# This code uses linear regression to plot an interpolated temperature vs volume curve,
# and identifies what element is represented by the curve. Code requires the
# periodic_table.json file from github to be uploaded into the Session 17 folder prior to running.

# Code is aided by that given by Dr. David Biersach in quadratic_regression_sklearn.py
# and plot_liquid_range.py.

# Code is also aided by the following online resources:
# https://uen.pressbooks.pub/introductorychemistry/chapter/molar-mass/#:~:text=The%20molar%20mass%20of%20any,mass%20is%2032.066%20g%2Fmol.
# https://flexbooks.ck12.org/cbook/ck-12-chemistry-flexbook-2.0/section/14.9/primary/lesson/calculating-the-molar-mass-of-a-gas-chem/


# If path errors arise, type-> cd "./Session 17 - Simulation and Modelling/" and
# then python ./identify_element.py ./periodic_table.json first before running.

# Used for type hinting
from __future__ import annotations

# For accessing json files
import json

# allows for type hints
import typing

# Used for plotting
import matplotlib.pyplot as plt

# Used for calculations
import numpy as np

# Used for linear regression calculations
from sklearn.linear_model import LinearRegression

if typing.TYPE_CHECKING:
    # Type hints for axes and arrays
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def fit_linear(
    vec_temp: NDArray[np.float_], vec_volume: NDArray[np.float_]
) -> tuple[float, float]:
    """Use the linear regression function to generate a line of best fit"""
    # Make vec_temp a 2d matrix
    vec_temp = vec_temp[:, np.newaxis]
    # Create a linear regression fit of vec_temp vs vec_volume
    model: LinearRegression = LinearRegression().fit(vec_temp, vec_volume)
    # slope is the first element of the model coefficients
    m: float = float(model.coef_[0])
    # b is the y intercept of the model
    b: float = float(model.intercept_)  # type: ignore
    # return slope and y-int
    return m, b


def find_element(
    vec_temp: NDArray[np.float_], vec_volume: NDArray[np.float_]
) -> tuple[str, str]:
    """Identify which element is represented by the data"""
    # Known values:
    mass: float = 50  # g
    pressure: float = 2.00  # atm
    mean_temp: float = sum(vec_temp) / len(vec_temp)  # kelvin
    mean_volume: float = sum(vec_volume) / len(vec_volume)  # m^3
    R: float = 0.08206  # L*atm/ K*mol
    # find mol-> n= PV/RT
    n: float = (pressure * mean_volume) / (R * mean_temp)
    # find molar mass from n and mass
    molar_mass: float = np.round((mass / n), 1)  # g/mol
    print(f"{molar_mass}")
    # use json periodic table
    # found on github
    with open("periodic_table.json", "r", encoding="utf-8") as infile:
        periodic_table = json.load(infile)
    # Sort elements by atomic number
    # list of tuples of 3 things [str, str, float]
    elements: list = []
    # enumerate over the entire periodic table
    for _, v in enumerate(periodic_table["elements"]):
        # append the name, symbol and atomic mass
        elements.append((f"{v['name']}", f"{v['symbol']}", v["atomic_mass"]))

    # Create numpy arrays from sorted elements list
    data = np.array(elements)
    # create array of atomic mass
    atomic_mass = np.array(data[:, 2], dtype=float)
    # for every mass in atomic mass
    for i, m in enumerate(atomic_mass):
        # if the value is close to the molar mass
        if abs(molar_mass - np.round(m, 1)) <= 0.01:
            # element is identified
            element: tuple[str, str] = (data[i, 0], data[i, 1])
            # return the identified element
            return element


def plot(ax: Axes) -> None:
    """Plot the given data set"""
    # create an array of temperatures
    vec_temp: NDArray[np.float_] = np.array([-50, 0, 50, 100, 150])
    # convert celsius to kelvin
    vec_temp = vec_temp + 273.15
    # Create an array of volumes
    vec_volume: NDArray[np.float_] = np.array([11.6, 14.0, 16.2, 19.4, 21.8])
    # convert to m^3 for the plot, but not for the find_element calculation
    vec_volume_convert = vec_volume / 1000
    # Define the minimum and maximum x values
    min_temp: float = float(np.min(vec_temp))
    max_temp: float = float(np.max(vec_temp))
    # Create an array of x's based on the min and max
    x: NDArray[np.float_] = np.linspace(min_temp, max_temp, 1000)
    # Initialize slope to a float
    m: float
    # Calculate slope and y-int using fit_linear
    m, b = fit_linear(vec_temp, vec_volume_convert)
    # Plot the linear regression curve
    ax.plot(x, m * x + b, label="Linear Fit")
    # Plot the actual data
    ax.scatter(vec_temp, vec_volume_convert, color="red", label="Actual Data")
    # Identify the element using the helper function
    element: tuple[str, str] = find_element(vec_temp, vec_volume)
    # Set the title based on the element
    ax.set_title(f"{element[0]} ({element[1]}) Gas")
    # Set labels using latex
    ax.set_xlabel(r"$Temperature\;(\degree K)$")
    ax.set_ylabel(r"$Volume\;(m^3)$")
    # Provide a legend
    ax.legend()


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
