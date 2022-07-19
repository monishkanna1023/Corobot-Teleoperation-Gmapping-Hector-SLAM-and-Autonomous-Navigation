#!/usr/bin/env python2

import rospy
import sensor_msgs
from sensor_msgs.msg import LaserScan

pub = rospy.Publisher('/filt_scan', LaserScan, queue_size=10)
filtscan=LaserScan()

def callback(msg):
    current_time=rospy.Time.now()
    filtscan.header.stamp=current_time
    filtscan.header.frame_id = 'laser'
    filtscan.angle_min = -1.222
    filtscan.angle_max = 1.222
    filtscan.angle_increment = msg.angle_increment
    filtscan.time_increment = msg.time_increment
    filtscan.range_min = msg.range_min
    filtscan.range_max = msg.range_max
    filtscan.scan_time = msg.scan_time
    filtscan.ranges = msg.ranges[0:40]
    filtscan.intensities = msg.intensities[0:400]

    #print(filtscan)
    pub.publish(filtscan)

def listener():
    rospy.init_node('filtered_scan')
    subv=rospy.Subscriber('/scan', LaserScan, callback)
    rospy.spin()

if __name__=='__main__':
    listener()
