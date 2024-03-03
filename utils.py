import numpy as np
import matplotlib.pyplot as plt
#important constants:
G = 6.6743E-11

#calculates the distance between 2 points in 3 dimensions
def distance(p1, p2):
    vect = p2 - p1
    return np.linalg.norm(vect)

#calculates the gravitational acceleration vectors (np arrays) given position and mass
def gravaccel(p1, p2, m1, m2):
    dist = distance(p1, p2)
    unitVect = (p2-p1)/dist
    fgrav = (G * m1 * m2)/(dist*dist)
    print(fgrav)
    accel1 = (fgrav/m1) * unitVect
    accel2 = (fgrav/m2) * unitVect * -1
    return accel1, accel2
