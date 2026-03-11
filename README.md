SHAPE DRAWER IN TURTLESIM
This is a midterm project on Microcontrollers for Robotics.
The project was completed in the ROS 2 program using the Turtlesim extension.

Technologies Used:
• ROS2 (Robot Operating System 2)
• Python 3
• turtlesim (2D turtle simulator)
• ROS Topics:
• /turtle1/cmd_vel — for publishing the turtle's speed (Twist)
• /turtle1/pose — for subscribing to the turtle's current position (Pose)

The project has one ROS2 node: TurtleDraw
Components of Node:
1. self.pub:  Publisher
2. self.pose_sub:  Subscriber
3. move_to(x, y):  Method
4. rotate_to(angle):   Method
5. move(linear, angular, duration):  Method 
6. draw_square():  Method 
7. draw_circle():  Method
8. draw_triangle(): METHOD

Structure:
~/turtle_project/
└── src/
    └── draw_shapes.py  


