import matplotlib.pyplot as plt


class Visualizer:
    # Handles plotting for the vehicle simulation.

    def __init__(self, simulation, path):
        self.simulation = simulation
        self.path = path

    # Plot reference path and vehicle trajectory
    def plot_path_tracking(self):
        plt.figure(figsize=(8,6))
        plt.plot(self.path.x, self.path.y, "--", linewidth=2, label="Reference Path")
        plt.plot(self.simulation.x_history, self.simulation.y_history, linewidth=2, label="Vehicle Path")
        plt.xlabel("X Position (m)")
        plt.ylabel("Y Position (m)")
        plt.title("MPC Path Tracking")
        plt.axis("equal")
        plt.grid(True)
        plt.legend()

    # Plot vehicle speed
    def plot_velocity(self):
        plt.figure(figsize=(8,4))
        plt.plot(self.simulation.velocity_history, color="green")
        plt.title("Vehicle Velocity")
        plt.xlabel("Time Step")
        plt.ylabel("Velocity (m/s)")
        plt.grid(True)

    # Plot steering commands
    def plot_steering(self):
        plt.figure(figsize=(8,4))
        plt.plot(self.simulation.steering_history, color="orange")
        plt.title("Steering Command")
        plt.xlabel("Time Step")
        plt.ylabel("Steering Angle (rad)")
        plt.grid(True)

    # Plot acceleration commands
    def plot_acceleration(self):
        plt.figure(figsize=(8,4))
        plt.plot(self.simulation.acceleration_history, color="red")
        plt.title("Acceleration Command")
        plt.xlabel("Time Step")
        plt.ylabel("Acceleration (m/s²)")
        plt.grid(True)

    # Plot path tracking error
    def plot_tracking_error(self):
        plt.figure(figsize=(8,4))
        plt.plot(self.simulation.error_history, color="purple")
        plt.title("Tracking Error")
        plt.xlabel("Time Step")
        plt.ylabel("Error (m)")
        plt.grid(True)

    # Display all figures
    def show(self):
        plt.show()