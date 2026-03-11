import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
import math

class TurtleDraw(Node):
    def __init__(self):
        super().__init__('turtle_draw')
        self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        time.sleep(1)  # небольшая пауза перед началом

        self.draw_square()
        self.move_forward(3.0)  # отступ перед следующей фигурой
        self.draw_circle()
        self.move_forward(3.0)  # ещё один отступ
        self.draw_triangle()

    def move(self, linear, angular, duration):
        msg = Twist()
        msg.linear.x = linear
        msg.angular.z = angular
        start = time.time()
        while time.time() - start < duration:
            self.pub.publish(msg)
            time.sleep(0.05)

    # Функция просто для перемещения вперёд (для отступов)
    def move_forward(self, distance):
        # скорость 1 м/с, время = distance / скорость
        duration = distance / 1.0
        self.move(1.0, 0.0, duration)

    def draw_square(self):
        for _ in range(4):
            self.move(1.0, 0.0, 2.0)       # вперед
            self.move(0.0, math.pi/2, 1.0) # поворот 90°

    def draw_circle(self):
        self.move(1.0, 1.0, 6.28)  # полный оборот

    def draw_triangle(self):
        for _ in range(3):
            self.move(1.0, 0.0, 2.0)
            self.move(0.0, math.pi/3, 1.0) # поворот 60°

def main(args=None):
    rclpy.init(args=args)
    node = TurtleDraw()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
