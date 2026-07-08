import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64MultiArray

import numpy as np


class VehicleNode(Node):

    def __init__(self):

        super().__init__("vehicle_node")


        # Vehicle parameters
        self.L = 2.8       # wheelbase
        self.dt = 0.1      # timestep


        # Vehicle state
        self.x = 0.0
        self.y = 0.0
        self.yaw = 0.0
        self.velocity = 0.0


        # Subscribe to controller commands
        self.subscription = self.create_subscription(
            Float64MultiArray,
            "/control_command",
            self.control_callback,
            10
        )


        # Publish vehicle state
        self.publisher = self.create_publisher(
            Float64MultiArray,
            "/vehicle_state",
            10
        )


        self.get_logger().info(
            "Vehicle node started"
        )


        # Timer for vehicle update
        self.timer = self.create_timer(
            self.dt,
            self.update_vehicle
        )


        # Store latest controls
        self.acceleration = 0.0
        self.steering = 0.0



    def control_callback(self, msg):

        # Receive:
        # msg.data[0] = acceleration
        # msg.data[1] = steering

        self.acceleration = msg.data[0]
        self.steering = msg.data[1]



    def update_vehicle(self):

        # Kinematic bicycle model

        self.x += (
            self.velocity *
            np.cos(self.yaw) *
            self.dt
        )


        self.y += (
            self.velocity *
            np.sin(self.yaw) *
            self.dt
        )


        self.yaw += (
            self.velocity /
            self.L *
            np.tan(self.steering) *
            self.dt
        )


        self.velocity += (
            self.acceleration *
            self.dt
        )


        # Publish vehicle state

        state = Float64MultiArray()

        state.data = [
            self.x,
            self.y,
            self.yaw,
            self.velocity
        ]

        self.publisher.publish(state)



def main(args=None):

    rclpy.init(args=args)

    node = VehicleNode()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()



if __name__ == "__main__":
    main()
