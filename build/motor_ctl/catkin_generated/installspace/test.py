#!/usr/bin/env python2

import math
from math import sin, cos, pi
import rospy
import tf
from nav_msgs.msg import Odometry
from std_msgs.msg import *
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3
from motor_ctl.msg import vel


vx = 0.0
vy = 0.0
vth = 0.0

lv = 0
rv = 0

def callback(msg):
    global lv, rv, vx, vth
    lv = msg.lv
    rv = msg.rv
    #vx = (lv + rv)/2
    #vth = (rv - lv)/0.27 #t: wheel base


rospy.init_node('odometry_publisher')

odom_pub = rospy.Publisher("odom", Odometry, queue_size=50)
vel_sub = rospy.Subscriber("velocity",vel, callback) 

odom_broadcaster = tf.TransformBroadcaster()

x = 0.0
y = 0.0
th = 0.0



current_time = rospy.Time.now()
last_time = rospy.Time.now()

r = rospy.Rate(1.0)
while not rospy.is_shutdown():
    current_time = rospy.Time.now()

    dl = lv*.25
    dr = rv*.25
    dc = (dl+dr)/2
    dt = .25 #250 ms in secs
    dth = (dr-dl)/0.39 #wheel track
    v_r = dr/dt
    v_l = dl/dt
    if dr==dl:
        dx = dr *cos(th)
        dy = dr *sin(th)

    else:
        radius = dc/dth

        iccX = x - radius*sin(th)
        iccY = y+radius*cos(th)
        
        dx = cos(dth) * (x-iccX) - sin(dth) * (y-iccY) + iccX - x
        dy = sin(dth) * (x-iccX) + cos(dth) * (y-iccY) + iccY - y


    x += dx
    y += dy
    th = (th+dth) % (2*pi)

    odom_quat = tf.transformations.quaternion_from_euler(0, 0, th)

    # first, we'll publish the transform over tf
    odom_broadcaster.sendTransform(
        (x, y, 0),
        odom_quat,
        current_time,
        "base_link",
        "odom"
    )

    # next, we'll publish the odometry message over ROS
    odom = Odometry()
    odom.header.stamp = current_time
    odom.header.frame_id = "odom"

    # set the position
    odom.pose.pose = Pose(Point(x, y, 0.), Quaternion(*odom_quat))

    if dt>0:
        vx = dx/dt
        vy = dy/dt
        vth = dth/dt

    # set the velocity
    odom.child_frame_id = "base_link"
    odom.twist.twist = Twist(Vector3(vx, vy, 0), Vector3(0, 0, vth))

    # publish the message
    odom_pub.publish(odom)

    last_time = current_time
    r.sleep()

