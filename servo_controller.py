import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import time
import math

class ServoIramaNode(Node):
    def __init__(self):
        super().__init__('servo_irama_node')
        self.publisher_ = self.create_publisher(Int32, 'servo_angle', 10)
        self.timer = self.create_timer(0.1, self.timer_callback) # Update setiap 0.1 detik
        self.start_time = time.time()
        self.get_logger().info('Node Pengontrol Servo Irama telah dimulai.')

    def timer_callback(self):
        msg = Int32()
        
        # Logika "Irama": Menggunakan fungsi Sinus agar gerakan halus bolak-balik
        elapsed = time.time() - self.start_time
        # Frekuensi 0.5Hz, amplitudo 0-180 derajat
        angle = int(90 + 90 * math.sin(2 * math.pi * 0.5 * elapsed))
        
        msg.data = angle
        self.publisher_.publish(msg)
        self.get_logger().info(f'Mengirim sudut: {angle}')

def main(args=None):
    rclpy.init(args=args)
    node = ServoIramaNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
