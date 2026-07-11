import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
from vehicle_simulation.mpc_controller import MPCController


class ControllerNode(Node):

    def __init__(self):
        super().__init__("controller_node")

        self.reference = None
        self.vehicle_state = [0.0, 0.0, 0.0, 0.0]
        self.mpc = MPCController()

        self.path_subscription = self.create_subscription(
            Float64MultiArray,
            "/reference_path",
            self.path_callback,
            10
        )

        self.state_subscription = self.create_subscription(
            Float64MultiArray,
            "/vehicle_state",
            self.state_callback,
            10
        )

        self.publisher = self.create_publisher(
            Float64MultiArray,
            "/control_command",
            10
        )

        self.get_logger().info("Controller node started with MPC")

    def path_callback(self, msg):
        self.reference = list(msg.data)

    def state_callback(self, msg):
        self.vehicle_state = list(msg.data)
        self.publish_control()

    def get_target_point(self):
        if self.reference is None:
            return None

        x, y = self.vehicle_state[0], self.vehicle_state[1]
        points = []

        for i in range(0, len(self.reference), 2):
            points.append(
                (self.reference[i], self.reference[i + 1])
            )

        nearest = 0
        min_distance = float("inf")

        for i, p in enumerate(points):
            d = (p[0] - x)**2 + (p[1] - y)**2
            if d < min_distance:
                min_distance = d
                nearest = i

        target_index = min(nearest + 10, len(points) - 1)

        return points[target_index]

    def publish_control(self):
        if self.reference is None:
            return

        target = self.get_target_point()

        if target is None:
            return

        try:
            control = self.mpc.solve(
                self.vehicle_state,
                target
            )

            # MPC output: [steering, acceleration]
            steering = float(control[0])
            acceleration = float(control[1])

        except Exception as e:
            self.get_logger().error(f"MPC failed: {e}")
            return

        command = Float64MultiArray()
        command.data = [
            acceleration,
            steering
        ]

        self.publisher.publish(command)

        self.get_logger().info(
            f"State x={self.vehicle_state[0]:.2f}, "
            f"Target x={target[0]:.2f}, "
            f"Accel={acceleration:.2f}, "
            f"Steer={steering:.2f}"
        )


def main(args=None):
    rclpy.init(args=args)
    node = ControllerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
