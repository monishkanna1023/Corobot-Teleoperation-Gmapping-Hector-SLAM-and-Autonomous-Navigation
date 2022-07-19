#!/usr/bin/env python2

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import numpy as np

global threshold
threshold=0.7

def cb_twist(msg):
    
    move.linear.x = msg.linear.x 
    move.linear.y = msg.linear.y
    move.linear.z = msg.linear.z

    move.angular.x = msg.angular.x
    move.angular.y = msg.angular.y
    move.angular.z = msg.angular.z     

  

  
def cb_scan(msg):
    global threshold
    
    #n=len(msg.ranges)

    mincur=np.min(msg.ranges)

    print(mincur)

    if mincur<threshold:
        
        move.linear.x = 0.0
        move.linear.y = 0.0
        move.linear.z = 0.0
        
        move.angular.x = 0.0
        move.angular.y = 0.0
        move.angular.z = 0.0

    else:
        pass

    pub_twist.publish(move)


rospy.init_node('obstacle_detect')

move=Twist()

sub_twist=rospy.Subscriber('/cmd_vel', Twist, cb_twist)

sub_scan=rospy.Subscriber('/filt_scan', LaserScan, cb_scan)

pub_twist=rospy.Publisher('/cmd_vel2', Twist, queue_size=1)

rate = rospy.Rate(2)


rospy.spin()

