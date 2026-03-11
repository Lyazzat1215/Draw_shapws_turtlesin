import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
import math

class TurtleDraw(Node):
    def __init__(self):
        super().__init__('turtle_draw')
        # Публикатор для движения черепашки
        self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        time.sleep(1)  # небольшая пауза перед началом
        self.draw_square()
        self.draw_circle()
        self.draw_triangle()

    # Функция движения: линейная и угловая скорость+длительность
    def move(self, linear, angular, duration):
        msg = Twist()
        msg.linear.x = linear
        msg.angular.z = angular
        start = time.time()
        while time.time() - start < duration:
            self.pub.publish(msg)
            time.sleep(0.05)

    def draw_square(self):
        for _ in range(4):
            self.move(1.0, 0.0, 2.0)       # forward
            self.move(0.0, math.pi/2, 1.0) # 90

    def draw_circle(self):
        self.move(1.0, 1.0, 6.28)  #360

    def draw_triangle(self):
        for _ in range(3):
            self.move(1.0, 0.0, 2.0)
            self.move(0.0, math.pi/3, 1.0) # 60°

def main(args=None):
    rclpy.init(args=args)
    node = TurtleDraw()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()