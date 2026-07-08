import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64MultiArray


class ControllerNode(Node):

    def __init__(self):

        super().__init__("controller_node")

        # Latest path reference
        self.reference = None

        # Latest vehicle state
        self.vehicle_state = None

        # Subscribe to planner output
        self.path_subscription = self.create_subscription(
            Float64MultiArray,
            "/reference_path",
            self.path_callback,
            10
        )

        # Subscribe to vehicle state
        self.state_subscription = self.create_subscription(
            Float64MultiArray,
            "/vehicle_state",
            self.state_callback,
            10
        )

        # Publish control commands
        self.publisher = self.create_publisher(
            Float64MultiArray,
            "/control_command",
            10
        )

        self.get_logger().info("Controller node started")

    def path_callback(self, msg):

        self.reference = msg.data

        self.publish_control()

    def state_callback(self, msg):

        self.vehicle_state = msg.data

    def publish_control(self):

        # Wait until we have both messages
        if self.reference is None:
            return

        if self.vehicle_state is None:
            return

        command = Float64MultiArray()

        # Placeholder commands (MPC will replace these next)
        command.data = [
            1.0,
            0.0
        ]

        self.publisher.publish(command)

        self.get_logger().info(
            f"Vehicle x={self.vehicle_state[0]:.2f}, "
            f"Target x={self.reference[0]:.2f}"
        )


def main(args=None):

    rclpy.init(args=args)

    node = ControllerNode()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()
