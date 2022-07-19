#!/usr/bin/env python2
import rospy
from std_msgs.msg import *

from Phidget22.Phidget import *
from Phidget22.Devices.Encoder import *
from Phidget22.Devices.DigitalInput import *
from Phidget22.Phidget import *
from Phidget22.Devices.Encoder import *
from motor_ctl.msg import vel

Po  = 0.00
v = vel()
v.lv = 0.00
v.rv = 0.00

def encoder_data():

    global Po,v, velCal
    
    encoder0 = Encoder()
    encoder0.setChannel(0)
    encoder0.openWaitForAttachment(5000)
    encoder0.setDataInterval(250)

    encoder1 = Encoder()
    encoder1.setChannel(1)
    encoder1.openWaitForAttachment(5000)
    encoder1.setDataInterval(250)

    def onPositionChange0(self, positionChange, timeChange, indexTriggered):
        global Po,v
        Po = positionChange
        v.rv = -(Po)*0.12/250
        

    def onPositionChange1(self, positionChange, timeChange, indexTriggered):
        global Po,v
        Po = positionChange
        v.lv = Po*0.12/250
        


    encoder0.setOnPositionChangeHandler(onPositionChange0)
    

    encoder1.setOnPositionChangeHandler(onPositionChange1)
    
    
    vel_RL = rospy.Publisher('velocity', vel, queue_size=10)
    rospy.init_node('encoder', anonymous=True)

    
    rate = rospy.Rate(10) 
    while not rospy.is_shutdown():
        vel_RL.publish(v)
        rate.sleep()


    encoder0.close()
    encoder1.close()

if __name__ == '__main__':
    try:
        encoder_data()
    except rospy.ROSInterruptException:
        pass






