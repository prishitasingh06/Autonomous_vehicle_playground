import numpy as np


class Metrics:
    # Computes performance metrics for the simulation.

    def __init__(self, simulation):
        self.simulation = simulation

    # Compute RMS tracking error
    def rms_tracking_error(self):
        errors = np.array(self.simulation.error_history)
        return np.sqrt(np.mean(errors**2))

    # Compute mean tracking error
    def mean_tracking_error(self):
        errors = np.array(self.simulation.error_history)
        return np.mean(errors)

    # Compute maximum tracking error
    def max_tracking_error(self):
        errors = np.array(self.simulation.error_history)
        return np.max(errors)

    # Get final tracking error
    def final_tracking_error(self):
        return self.simulation.error_history[-1]

    # Compute average vehicle speed
    def average_speed(self):
        speeds = np.array(self.simulation.velocity_history)
        return np.mean(speeds)

    # Compute maximum vehicle speed
    def maximum_speed(self):
        speeds = np.array(self.simulation.velocity_history)
        return np.max(speeds)

    # Print performance summary
    def summary(self):
        print("\n*************************")
        print(" MPC Performance Summary")
        print("*************************")
        print(f"RMS Tracking Error   : {self.rms_tracking_error():.3f} m")
        print(f"Mean Tracking Error  : {self.mean_tracking_error():.3f} m")
        print(f"Maximum Error        : {self.max_tracking_error():.3f} m")
        print(f"Final Error          : {self.final_tracking_error():.3f} m")
        print(f"Average Speed        : {self.average_speed():.3f} m/s")
        print(f"Maximum Speed        : {self.maximum_speed():.3f} m/s")
        print("*************************\n")