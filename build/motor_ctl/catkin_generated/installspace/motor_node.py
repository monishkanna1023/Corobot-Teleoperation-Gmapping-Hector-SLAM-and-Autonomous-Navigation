#!/usr/bin/env python2
import rospy
from std_msgs.msg import Float32



def motor_vel():
    lvel_pub = rospy.Publisher('lmotor_cmd', Float32, queue_size=10)
    rvel_pub = rospy.Publisher('rmotor_cmd', Float32, queue_size=10)
    rospy.init_node('motor_vel', anonymous=True)
    robotrate = 10
    rate = rospy.Rate(robotrate)

    while not rospy.is_shutdown():
        lvel_pub.publish(0.2)
        rvel_pub.publish(0.5)
        rate.sleep()


if __name__ == '__main__':
    try:
        motor_vel()
    except rospy.ROSInterruptException:
        pass