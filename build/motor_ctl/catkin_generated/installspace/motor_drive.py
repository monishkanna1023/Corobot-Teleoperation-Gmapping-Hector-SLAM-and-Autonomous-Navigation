#!/usr/bin/env python2
from runpy import run_module
import rospy
from std_msgs.msg import Float32
from Phidget22.Phidget import *
from Phidget22.Devices.DCMotor import *
from Phidget22.PhidgetException import *
import time

lmotor = DCMotor()
rmotor = DCMotor()

def onError(self, code, description):
    pass

def lmover(lv):
    while not rospy.is_shutdown():
        rospy.loginfo("left wheel velocity received (%f)", lv.data)
        lmotor.setTargetVelocity(lv.data)

def rmover(rv):
    while not rospy.is_shutdown():
        rospy.loginfo("right wheel velocity received (%f)", rv.data)
        rmotor.setTargetVelocity(rv.data)


def driver():
    lmotor.setChannel(0)
    rmotor.setChannel(1)

    lmotor.setOnErrorHandler(onError)
    rmotor.setOnErrorHandler(onError)

    lmotor.openWaitForAttachment(5000)
    rmotor.openWaitForAttachment(5000)

    rospy.init_node('motor_driver', anonymous=True)
    rospy.Subscriber('lmotor_cmd', Float32, lmover)
    rospy.Subscriber('rmotor_cmd', Float32, rmover)

    rospy.spin()

    lmotor.close()
    rmotor.close()
    
driver()


