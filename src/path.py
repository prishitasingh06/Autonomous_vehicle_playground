import numpy as np


class Path:
    def __init__(self):

        self.x = np.linspace(0, 50, 200)

        # Creating curved road
        self.y = 5 * np.sin(self.x / 10)


    def get_points(self):
        return self.x, self.y