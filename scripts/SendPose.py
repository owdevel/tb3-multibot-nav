#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from tf.transformations import quaternion_from_euler

rospy.init_node('init_pos')
pub = rospy.Publisher('/tb3_0/initialpose', PoseWithCovarianceStamped, queue_size = 10)
rospy.sleep(1)
checkpoint = PoseWithCovarianceStamped()

checkpoint.pose.pose.position.x = -2.0
checkpoint.pose.pose.position.y = -0.5
checkpoint.pose.pose.position.z = 0.0

[x,y,z,w]=quaternion_from_euler(0.0,0.0,0.0)
checkpoint.pose.pose.orientation.x = x
checkpoint.pose.pose.orientation.y = y
checkpoint.pose.pose.orientation.z = z
checkpoint.pose.pose.orientation.w = w

checkpoint.header.frame_id = "map"

print(checkpoint)
pub.publish(checkpoint)