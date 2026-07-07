import numpy as np


class Path:

    def __init__(self):
        # Generate path X coordinates from 0 to 50 meters
        self.x = np.linspace(0, 50, 200)

        # Generate sinusoidal path:  y = 5sin(x/10)
        self.y = 5 * np.sin(self.x / 10)


    def get_closest_point(self, vehicle_x, vehicle_y):
        # Calculate distance from vehicle to every path point: d = sqrt((x2-x1)^2 + (y2-y1)^2)
        distance = np.sqrt((self.x - vehicle_x)**2 + (self.y - vehicle_y)**2)

        # Find index of the closest path point
        index = np.argmin(distance)

        # Return closest point coordinates
        return self.x[index], self.y[index]