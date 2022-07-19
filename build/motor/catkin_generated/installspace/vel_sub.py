#!/usr/bin/env python2
import rospy, roslib
from Phidget22.Phidget import *
from Phidget22.PhidgetException import *
import time
from Phidget22.Devices.DCMotor import *

from std_msgs.msg import Float32


motor1 = DCMotor()
motor2 = DCMotor()

def onError(self, code, description):
    pass

def mover(Data):
    while not rospy.is_shutdown():
        
        motor1.setTargetVelocity(Data.data)
        motor2.setTargetVelocity(Data.data)
        print(Data.data)

        try:
            input("Press Enter to Stop")
        except(Exception, KeyboardInterrupt):
            motor1.close()
            motor2.close()
            exit()
                




def driver():


    motor1.setChannel(0)
    motor2.setChannel(1)

    motor1.setOnErrorHandler(onError)
    motor1.setOnErrorHandler(onError)

    motor1.openWaitForAttachment(5000)
    motor2.openWaitForAttachment(5000)


    rospy.init_node('motor_driver', anonymous=True)
    rospy.Subscriber('velocity_pub', Float32, mover)
    rospy.spin()

driver()
