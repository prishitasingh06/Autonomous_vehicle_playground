import numpy as np


class Simulation:

    def __init__(self, vehicle, dt=0.1, duration=20):

        self.vehicle = vehicle
        self.dt = dt
        self.duration = duration

        self.time = []
        self.x_history = []
        self.y_history = []
        self.yaw_history = []
        self.velocity_history = []


    def run(self, acceleration, steering):

        steps = int(self.duration / self.dt)

        for i in range(steps):

            current_time = i * self.dt

            self.vehicle.update(
                acceleration,
                steering,
                self.dt
            )

            state = self.vehicle.state()

            self.time.append(current_time)

            self.x_history.append(state[0])
            self.y_history.append(state[1])
            self.yaw_history.append(state[2])
            self.velocity_history.append(state[3])


    def get_results(self):

        return {
            "time": np.array(self.time),
            "x": np.array(self.x_history),
            "y": np.array(self.y_history),
            "yaw": np.array(self.yaw_history),
            "velocity": np.array(self.velocity_history)
        }