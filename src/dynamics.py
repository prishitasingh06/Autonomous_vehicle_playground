import numpy as np

# Why we created dynamics.py?
# Before:
# Vehicle class
#      |
#      ↓
# Movement

# Now:

# Vehicle Model
#        |
#        ↓
# Dynamics Equation
#        |
#        ↓
# MPC Prediction

# MPC needs equations it can predict with.

class VehicleDynamics:


    # Initialize vehicle parameters
    def __init__(self):

        # Distance between front and rear axle (wheelbase)
        # Used in the bicycle vehicle model
        self.L = 2.8


    # Update vehicle state using the kinematic bicycle model
    #
    # state:
    #   [x, y, yaw, v]
    #
    #   x   -> vehicle X position (meters)
    #   y   -> vehicle Y position (meters)
    #   yaw -> vehicle heading angle (radians)
    #   v   -> vehicle velocity (m/s)
    #
    # control: [acceleration, steering]
    #   acceleration -> change in velocity (m/s^2)
    #   steering     -> front wheel steering angle (radians)
    #
    # dt: simulation time step (seconds)
    def update(self, state, control, dt):


        # Extract current vehicle state
        x, y, yaw, v = state


        # Extract control inputs
        acceleration, steering = control


        # Update X position
        #
        # Vehicle moves in the direction of its heading:
        #
        #        yaw
        #         /
        #        /
        #       *
        #
        # x velocity component = v*cos(yaw)
        #
        x_new = x + v * np.cos(yaw) * dt


        # Update Y position
        # y velocity component = v*sin(yaw)
        y_new = y + v * np.sin(yaw) * dt


        # Update vehicle heading (yaw)
        # Bicycle model equation: yaw_rate = (v/L) * tan(steering)
        # Larger steering angle -->faster rotation.
        # L is the vehicle wheelbase.
        yaw_new = yaw + (
            (v / self.L) * np.tan(steering)
        ) * dt


        # Update velocity
        # New velocity = old velocity + acceleration*time
        # Positive acceleration increases speed.
        # Negative acceleration slows the vehicle down.
        v_new = v + acceleration * dt


        # Return updated vehicle state
        # New state: [new x position,new y position,new heading angle,new velocity]
        return np.array([
            x_new,
            y_new,
            yaw_new,
            v_new
        ])
    

