import Math
import numpy as np
import matplotlib.pyplot as plt

# in order to solve the lost in space problem, we must be able to do a few things:
# 1. Identify the locations of the planets (image recognition)
# 2. Know where the planets should be relative to a certain point (eart, sun, etc.)
# 3. Use that information to determine spacecraft location

# 2 -> Developing a model of our solar system using python

G = 6.6743E-11

#calculates the distance between 2 points in 3 dimensions
def distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return 0

#calculates the gravitational acceleration given position and mass
def gravaccel(p1, p2, m1, m2):
    return 0


print("hello world")