import numpy as np

class Body:

    def __init__(self, name, position, velocity, acceleration, mass):
        self.name = name
        self.postion = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.mass = mass

    def propogate(self, newAcceleration, timestep):
        self.acceleration = newAcceleration
        newVelocity = self.velocity + self.acceleration * timestep
        newPosition = self.postion + (self.velocity + newVelocity * timestep)/2
        self.velocity = newVelocity
        self.postion = newPosition


    