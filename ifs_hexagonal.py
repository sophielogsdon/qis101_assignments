#!/usr/bin/env python3
"""ifs_hexagonal.py"""

# This code uses an IFS to reproduce a hexagonal output.

# Code is modified from that given by Dr. David Biersach in ifs_square.py.

# Used for calculations
import numpy as np

# set of 2D affine transforms
# python class that will specify these 3 transformation matrices
# need to identify which 3 points you want
from ifs import IteratedFunctionSystem

# Used for plotting in pygame
from pygame import Color

# Used to convert to world coordinates
from simple_screen import SimpleScreen

ifs = IteratedFunctionSystem()


def plot_ifs(ss: SimpleScreen) -> None:
    """Plot the ifs for the 3 input data points"""
    # 200,000 dots that are being drawn
    # just a single point jumping around 200,00x in a phase space
    iterations = 200_000
    # Initialize x,y and color variables
    x: float = 0.0
    y: float = 0.0
    clr: Color

    # Iterate (but don't draw) to let IFS reach its stable orbit
    # old xy becomes new xy over and over again
    # gives us a valid xy starting point so we can reach the strange attractor
    for _ in range(100):
        x, y, clr = ifs.transform_point(x, y)

    # Now draw each pixel in the stable orbit
    # Only plot the end result, so we don't see the dots jumping around randomly
    for _ in range(iterations):
        x, y, clr = ifs.transform_point(x, y)
        ss.set_world_pixel(x, y, clr)


def main() -> None:
    """Define an entry point for the function"""

    # tell ifs the size of your original image
    # cartesian coordinates (0,0) to (30,30)
    ifs.set_base_frame(0, 0, 30, 30)
    # uniform probability
    # probability that a matrix will be selected
    p: float = 1 / 6

    # 6 transformations, all in blue
    # specify where we want bottom left, bottom right and top left to go
    # xy xy xy -> 6 values total
    # COD
    ifs.add_mapping(25, 15, 15, 15, 20, 23.66, Color("blue"), p)
    # DOE
    ifs.add_mapping(20, 23.66, 15, 15, 10, 23.66, Color("blue"), p)
    # EOF
    ifs.add_mapping(10, 23.66, 15, 15, 5, 15, Color("blue"), p)
    # FOA
    ifs.add_mapping(5, 15, 15, 15, 10, 6.34, Color("blue"), p)
    # AOB
    ifs.add_mapping(10, 6.34, 15, 15, 20, 6.34, Color("blue"), p)
    # BOC
    ifs.add_mapping(20, 6.34, 15, 15, 25, 15, Color("blue"), p)

    # helper function that will generate these matrices
    ifs.generate_transforms()

    # Convert to world coordinates
    # world_rect= size of image
    # screen_size- for older computers
    # draw_func- tell it what function to plot
    ss = SimpleScreen(
        world_rect=((0, 0), (30, 30)),
        screen_size=(900, 900),
        draw_function=plot_ifs,
        title="IFS Hexagon",
    )
    # Show the ifs using simple screen helper function
    ss.show()


if __name__ == "__main__":
    """Call the main function"""
    main()
