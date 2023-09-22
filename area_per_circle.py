#!/usr/bin/env python3

# Created By: Julien Lamoureux
# Date: September 22, 2023
# This program calculates the area and circumference of a circle with a radius of 3.5


import math


def main():
    radius = 3.5
    circumference = 2 * math.pi * radius
    area_of_circle = math.pi * radius**2
    print("A circle that has a radius of :")
    print("3.5 cm")
    print("")
    print("Given these dimensions, the Area = {:.2f} cm^2".format(area_of_circle))
    print("And the Circumference = {:.2f} cm".format(circumference))


if __name__ == "__main__":
    main()
