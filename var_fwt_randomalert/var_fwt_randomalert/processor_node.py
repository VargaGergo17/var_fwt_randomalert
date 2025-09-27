import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class ProcessorNode(Node):
    def __init__(self):
        super().__init__('processor_node')
        self.subscription = self.create_subscription(
            String,
            'chatter',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        processed = msg.data.upper()  
        self.get_logger().info(f'Received: "{msg.data}" | Processed: "{processed}"')


def main(args=None):
    rclpy.init(args=args)
    node = ProcessorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
