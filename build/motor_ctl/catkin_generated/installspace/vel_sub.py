#!/usr/bin/env python2
import rospy
from motor_ctl.msg import vel
from Phidget22.Phidget import *
from Phidget22.PhidgetException import *
import time
from Phidget22.Devices.DCMotor import *

motor1 = DCMotor()
motor2 = DCMotor()



def onError(self, code, description):
    pass


def mover(velocity_msg):
    while not rospy.is_shutdown():
        rospy.loginfo("velocity data received (%f, %f)", velocity_msg.lv, velocity_msg.rv)

        
        motor1.setTargetVelocity(velocity_msg.lv)
        motor2.setTargetVelocity(velocity_msg.rv)

        


def driver():
    motor1.setChannel(0)
    motor2.setChannel(1)

    motor1.setOnErrorHandler(onError)
    motor1.setOnErrorHandler(onError)

    motor1.openWaitForAttachment(5000)
    motor2.openWaitForAttachment(5000)

    rospy.init_node('velocity_subscriber', anonymous=True)
    rospy.Subscriber('velocity_pub', vel, mover)
    rospy.spin()

    motor1.close()
    motor2.close()




driver()
