#!/usr/bin/env python
import roslib
import rospy
import tf.transformations
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32
from Phidget22.Phidget import *
from Phidget22.Devices.DCMotor import *
from Phidget22.PhidgetException import *
import time

t = 0.27
#t is the wheel base of corobot


lmotor = DCMotor()
rmotor = DCMotor()
lmotor.setChannel(1)
rmotor.setChannel(0)
lmotor.openWaitForAttachment(5000)
rmotor.openWaitForAttachment(5000)

def cstm_vel(mps_vel):
    v = (mps_vel+0.0085)/1.6
    #from the function y=1.6x-0.0085 where y is velocity in m/s
    v = sorted([-0.5,v,0.5])[1]
    return v




def callback(msg):
    rospy.loginfo("Received a vel message!")
    rospy.loginfo("Linear Components: [%f, %f, %f]"%(msg.linear.x, msg.linear.y, msg.linear.z))
    rospy.loginfo("Angular Components: [%f, %f, %f]"%(msg.angular.x, msg.angular.y, msg.angular.z))

    
    x = msg.linear.x
    z = msg.angular.z

    lv = x - (z*t)/2
    rv = x + (z*t)/2

    lmotor.setTargetVelocity(cstm_vel(lv))
    rmotor.setTargetVelocity(cstm_vel(rv))


    
def listener():
    rospy.init_node('cmd_vel_listener', anonymous=True)
    rospy.Subscriber("/cmd_vel", Twist, callback)
    rospy.Subscriber("/cmd_vel2", Twist, callback)
    rospy.spin()  
    lmotor.close()
    rmotor.close()

if __name__ == '__main__':
    listener()
