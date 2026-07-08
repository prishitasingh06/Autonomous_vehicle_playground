import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
import numpy as np

class PlannerNode(Node):
    def __init__(self):
        super().__init__("planner_node")

        self.publisher = self.create_publisher(
            Float64MultiArray,
            "/reference_path",
            10
        )

        self.timer = self.create_timer(1.0, self.publish_path)

        self.get_logger().info("Planner node started")

    def publish_path(self):
        msg = Float64MultiArray()
        path = []

        x_values = np.linspace(0, 50, 200)

        for x in x_values:
            y = 5 * np.sin(x / 10)
            path.append(float(x))
            path.append(float(y))

        msg.data = path
        self.publisher.publish(msg)

        self.get_logger().info("Reference path published")

def main(args=None):
    rclpy.init(args=args)

    node = PlannerNode()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
