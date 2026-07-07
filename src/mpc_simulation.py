import numpy as np


class MPCSimulation:

    def __init__(self, vehicle, controller, path):

        self.vehicle = vehicle
        self.controller = controller
        self.path = path

        self.dt = 0.1

        # Vehicle history
        self.x_history = []
        self.y_history = []
        self.yaw_history = []
        self.velocity_history = []

        # MPC analysis history
        self.steering_history = []
        self.acceleration_history = []
        self.error_history = []


    def run(self, steps):

        for _ in range(steps):

            state = np.array([
                self.vehicle.x,
                self.vehicle.y,
                self.vehicle.yaw,
                self.vehicle.velocity
            ])


            reference = self.path.get_closest_point(
                self.vehicle.x,
                self.vehicle.y
            )


            control = self.controller.solve(
                state,
                reference
            )


            acceleration = control[0]
            steering = control[1]


            # Save controller commands
            self.acceleration_history.append(acceleration)
            self.steering_history.append(steering)


            # Update vehicle
            self.vehicle.update(
                acceleration,
                steering,
                self.dt
            )


            # Calculate tracking error
            error = np.sqrt(
                (self.vehicle.x - reference[0])**2 +
                (self.vehicle.y - reference[1])**2
            )

            self.error_history.append(error)


            # Save vehicle state
            self.x_history.append(self.vehicle.x)
            self.y_history.append(self.vehicle.y)
            self.yaw_history.append(self.vehicle.yaw)
            self.velocity_history.append(self.vehicle.velocity)