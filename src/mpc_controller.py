import casadi as ca
import numpy as np


class MPCController:

    def __init__(self):
        self.N = 10       # Prediction horizon (number of future steps)
        self.dt = 0.1     # Time step between predictions
        self.L = 2.8      # Vehicle wheelbase


    def solve(self, state, reference):
        """
        Solve MPC optimization problem.

        state: [x, y, yaw, velocity] -> current vehicle state
        reference: [x, y] -> desired target position
        """

        opti = ca.Opti()  # Create optimization problem


        # Optimization variables:
        # X stores predicted states: [x, y, yaw, velocity]
        # U stores control inputs: [acceleration, steering]
        X = opti.variable(4, self.N+1)
        U = opti.variable(2, self.N)

        # Extract state variables
        x, y, yaw, v = X[0,:], X[1,:], X[2,:], X[3,:]

        # Extract control variables
        acceleration, steering = U[0,:], U[1,:]


        # Force first predicted state to equal current vehicle state
        opti.subject_to(X[:,0] == state)


        # Vehicle prediction using kinematic bicycle model
        for k in range(self.N):

            # Predict next vehicle position
            x_next = x[k] + v[k]*ca.cos(yaw[k])*self.dt
            y_next = y[k] + v[k]*ca.sin(yaw[k])*self.dt

            # Predict heading change based on steering angle
            yaw_next = yaw[k] + (v[k]/self.L)*ca.tan(steering[k])*self.dt

            # Predict velocity change based on acceleration
            v_next = v[k] + acceleration[k]*self.dt

            # Apply vehicle dynamics constraint
            opti.subject_to(X[:,k+1] == ca.vertcat(x_next, y_next, yaw_next, v_next))


        # Cost function: minimize tracking error and control effort
        cost = 0

        for k in range(self.N):

            # Penalize distance from desired reference position
            cost += (x[k]-reference[0])**2 + (y[k]-reference[1])**2

            # Penalize large steering and acceleration inputs
            cost += 0.1*steering[k]**2 + 0.1*acceleration[k]**2

        opti.minimize(cost)


        # Steering constraints (maximum steering angle)
        opti.subject_to(steering <= 0.5)
        opti.subject_to(steering >= -0.5)

        # Acceleration constraints (maximum acceleration/braking)
        opti.subject_to(acceleration <= 2)
        opti.subject_to(acceleration >= -2)


        # Use IPOPT nonlinear optimization solver
        opti.solver("ipopt")

        # Solve optimization problem
        solution = opti.solve()

        # Return first control action from optimized sequence
        control = solution.value(U[:,0])

        return control
    
