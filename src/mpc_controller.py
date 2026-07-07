import casadi as ca
import numpy as np



class MPCController:


    def __init__(self):

        self.horizon = 10
        self.dt = 0.1


    def compute_control(self, state, reference):

        """
        Placeholder MPC controller.

        Optimization will be added next.
        """

        acceleration = 0.0
        steering = 0.0


        return np.array([
            acceleration,
            steering
        ])