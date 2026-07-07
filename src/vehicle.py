import numpy as np


class Vehicle:
    """
    Kinematic bicycle model vehicle.

    State:
        x     : x position (m)
        y     : y position (m)
        yaw   : heading angle (rad)
        v     : velocity (m/s)

    Inputs:
        acceleration : longitudinal acceleration (m/s^2)
        steering     : steering angle (rad)
    """

    def __init__(self, x=0.0, y=0.0, yaw=0.0, velocity=0.0):

        self.x = x
        self.y = y
        self.yaw = yaw
        self.velocity = velocity

        # Distance between front and rear axle
        self.wheelbase = 2.8


    def update(self, acceleration, steering, dt):

        # Update position
        self.x += self.velocity * np.cos(self.yaw) * dt
        self.y += self.velocity * np.sin(self.yaw) * dt

        # Update heading
        self.yaw += (
            self.velocity / self.wheelbase
        ) * np.tan(steering) * dt

        # Update velocity
        self.velocity += acceleration * dt


    def state(self):

        return [
            self.x,
            self.y,
            self.yaw,
            self.velocity
        ]