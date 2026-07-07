import numpy as np


class PurePursuitController:

    def __init__(self, look_ahead=3.0):
    # Initialize the controller
    # look_ahead defines how far ahead on the path the controller should look for the target point
        self.look_ahead = look_ahead


    def compute_steering(self, vehicle, path):
    # Calculate the steering angle required to follow the path
    #
    # vehicle:
    #   Object containing current vehicle state:
    #   vehicle.x   -> current X position
    #   vehicle.y   -> current Y position
    #   vehicle.yaw -> current heading angle
    #
    # path:
    #   Object containing path points:
    #   path.x -> array of X coordinates
    #   path.y -> array of Y coordinates
        
        # Calculate distance from the vehicle to every point on the path
        # Formula: distance = sqrt((x2-x1)^2 + (y2-y1)^2)
        # This creates an array containing the distance from the vehicle to each path point
        distances = np.sqrt(
            (path.x - vehicle.x)**2 + (path.y - vehicle.y)**2
        )

        # Find the index of the closest point on the path
        # np.argmin() returns the index where the distance value is the smallest
        closest_index = np.argmin(distances)

        # Select a point ahead of the closest point
        # Instead of steering toward the nearest point, Pure Pursuit looks ahead to a future point.
        # Here, the controller simply chooses a point 10 steps ahead on the path.
        target_index = closest_index + 10

        # Prevent going beyond the end of the path
        # If the target index is outside the path array,use the final path point instead
        if target_index >= len(path.x):
            target_index = len(path.x)-1

        # Get the coordinates of the target point
        target_x = path.x[target_index]
        target_y = path.y[target_index]

        # Calculate the angle from the vehicle position to the target point --->(The result is in radians)
        # arctan2 gives the angle of the vector:
        #
        #        target
        #          *
        #         /
        #        /
        #       *
        #    vehicle

        angle = np.arctan2(
            target_y - vehicle.y,target_x - vehicle.x
        )

        # Calculate the steering command
        # Steering = desired direction - current vehicle heading
        # If:
        #   steering > 0  --> turn left
        #   steering < 0  --> turn right
        # vehicle.yaw is subtracted because the vehicle already has its own heading direction
        steering = angle - vehicle.yaw
        return steering