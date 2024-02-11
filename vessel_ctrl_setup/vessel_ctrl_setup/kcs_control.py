import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32MultiArray

class TeleopTwistToFloatArray(Node):
    def __init__(self):
        super().__init__('kcs_teleop_twist_to_float_array')
        self.publisher = self.create_publisher(Float32MultiArray, '/kcs/commands', 10)
        self.subscription = self.create_subscription(Twist, '/cmd_vel', self.callback, 10)
        print("teleop_twist_keyboard to Float32MultiArray")

    def callback(self, twist_msg):
        float_array = Float32MultiArray()
        float_array.data = [
            float(twist_msg.angular.z),
            float(twist_msg.linear.x)
        ]
        self.publisher.publish(float_array)

def main(args=None):
    rclpy.init(args=args)
    twist_to_float_array = TeleopTwistToFloatArray()
    rclpy.spin(twist_to_float_array)
    twist_to_float_array.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
