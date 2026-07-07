import matplotlib.pyplot as plt
import numpy as np


class Visualizer:

    def __init__(self):

        self.fig, self.ax = plt.subplots(figsize=(8, 8))
        # fig → the entire window., ax → the actual plotting area.

        self.ax.set_xlabel("X Position (m)")
        self.ax.set_ylabel("Y Position (m)")

        self.ax.grid(True)
        self.ax.axis("equal")


    def draw_vehicle(self, vehicle):

        length = 4.5
        width = 2.0


        # Vehicle shape in local coordinates
        corners = np.array([
            [ length/2,  width/2],
            [ length/2, -width/2],
            [-length/2, -width/2],
            [-length/2,  width/2]
        ])


        # Rotation matrix
        rotation = np.array([
            [np.cos(vehicle.yaw), -np.sin(vehicle.yaw)],
            [np.sin(vehicle.yaw),  np.cos(vehicle.yaw)]
        ])


        # Convert vehicle coordinates to world coordinates
        vehicle_shape = corners @ rotation.T

        vehicle_shape[:,0] += vehicle.x
        vehicle_shape[:,1] += vehicle.y


        # Draw vehicle
        self.ax.fill(
            vehicle_shape[:,0],
            vehicle_shape[:,1],
            color="blue",
            alpha=0.5
        )


        # Draw heading arrow
        self.ax.arrow(
            vehicle.x,
            vehicle.y,
            np.cos(vehicle.yaw),
            np.sin(vehicle.yaw),
            color="red",
            width=0.05,
            head_width=0.3
        )