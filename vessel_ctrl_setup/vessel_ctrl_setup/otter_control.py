import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32MultiArray

class TeleopTwistToFloatArray(Node):
    def __init__(self):
        super().__init__('otter_teleop_twist_to_float_array')
        self.publisher = self.create_publisher(Float32MultiArray, '/otter/commands', 10)
        self.subscription = self.create_subscription(Twist, '/cmd_vel', self.callback, 10)
        print("teleop_twist_keyboard to Float32MultiArray")

    def callback(self, twist_msg):
        v_x = twist_msg.linear.x
        v_z = twist_msg.angular.z
        if v_z == 0.0:
            self.value(v_x,v_x)
        elif v_x == 0.0:
            if v_z <0.0:
                self.value(v_z,0.0)
            else:
                self.value(0.0,v_z)
        else:
            if v_z <0.0:
                self.value(v_x+v_z,v_x)
            else:
                self.value(v_x,v_z+v_x)
        
    def value(self, p1, p2):
        float_array = Float32MultiArray()
        float_array.data = [
            float(p1),
            float(p2)
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
# -*- coding: utf-8 -*-

