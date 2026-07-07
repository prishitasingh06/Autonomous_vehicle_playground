import numpy as np


class MPCSimulation:

    def __init__(self, vehicle, controller, path):
        # Store vehicle, MPC controller, and reference path
        self.vehicle = vehicle
        self.controller = controller
        self.path = path

        # Simulation time step
        self.dt = 0.1

        # Store vehicle history for plotting and analysis
        self.x_history = []
        self.y_history = []
        self.yaw_history = []
        self.velocity_history = []


    def run(self, steps):

        # Run simulation for given number of steps
        for _ in range(steps):

            # Get current vehicle state:
            # [x position, y position, yaw angle, velocity]
            state = np.array([
                self.vehicle.x,
                self.vehicle.y,
                self.vehicle.yaw,
                self.vehicle.velocity
            ])

            # Find target point on path
            reference = self.path.get_closest_point(
                self.vehicle.x,
                self.vehicle.y
            )

            # MPC calculates optimal control:
            # control[0] = acceleration
            # control[1] = steering angle
            control = self.controller.solve(state, reference)

            acceleration = control[0]
            steering = control[1]

            # Apply control inputs and update vehicle state
            self.vehicle.update(
                acceleration,
                steering,
                self.dt
            )

            # Save updated vehicle state for visualization
            self.x_history.append(self.vehicle.x)
            self.y_history.append(self.vehicle.y)
            self.yaw_history.append(self.vehicle.yaw)
            self.velocity_history.append(self.vehicle.velocity)