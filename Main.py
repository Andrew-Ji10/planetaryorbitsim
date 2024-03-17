import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
import body
import utils

# in order to solve the lost in space problem, we must be able to do a few things:
# 1. Identify the locations of the planets (image recognition)
# 2. Know where the planets should be relative to a certain point (eart, sun, etc.)
# 3. Use that information to determine spacecraft location

# 2 -> Developing a model of our solar system using python


# TODO generate ploting info
#print(utils.gravaccel(np.array([0,0,0]), np.array([6378100,0,0]), 100, 5.97219E+24))

b1 = body.Body("earth", np.array([384400000,0,0]), np.array([0,0,0]), np.array([0,0,0]), 5.97219E+24)
b2 = body.Body("moon", np.array([0,0,0]), np.array([0,1023,0]), np.array([0,0,0]), 7.36E+22)
#b1.displayState()
#b2.displayState()
bodies = np.array([b1, b2])
utils.integrate(np.array([b1, b2]), 5000000, 10000)
#b1.displayState()
#b2.displayState()
#print(b1.locations.T)
#print(b2.locations.T)

utils.animatebodies(bodies, 10000, 10, step=10)

'''
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

lines = np.array([])
for b in bodies:
    data = b.locations.T
    ln, = ax.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1], label=b.name)
    lines = np.append(lines, np.array([ln]))
print(lines)
'''
#utils.plotbodies(np.array([b1, b2]))

"""
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

def update(num, data, line):
    line.set_data(data[:2, :num*10])
    line.set_3d_properties(data[2, :num*10])

N = 1000
data = b2.locations.T
print(data)
line, = ax.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1])

# Setting the axes properties
ax.set_xlim3d([-1E+2, 1E+9])
ax.set_xlabel('X')

ax.set_ylim3d([-1E+9, 1E+9])
ax.set_ylabel('Y')

ax.set_zlim3d([-1.0, 10.0])
ax.set_zlabel('Z')

ani = animation.FuncAnimation(fig, update, N, fargs=(data, line), interval=100/N, blit=False)
#ani.save('matplot003.gif', writer='imagemagick')
plt.show()
"""