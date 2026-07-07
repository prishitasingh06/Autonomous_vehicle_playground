import numpy as np


class Path:

    def __init__(self):
        # Generate path X coordinates from 0 to 50 meters
        self.x = np.linspace(0, 50, 200)

        # Generate sinusoidal path:  y = 5sin(x/10)
        self.y = 5 * np.sin(self.x / 10)


    def get_closest_point(self, vehicle_x, vehicle_y):

        # Calculate distance from vehicle to every path point
        distance = np.sqrt((self.x - vehicle_x)**2 +(self.y - vehicle_y)**2)


        # Find closest path index
        index = np.argmin(distance)


        # Look ahead along the path
        target_index = index + 20


        # Prevent going outside path
        if target_index >= len(self.x):
            target_index = len(self.x) - 1


        # Return future target point
        return (self.x[target_index],self.y[target_index]
        )