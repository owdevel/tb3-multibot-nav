#!/usr/bin/env python

import argparse
import rospy
from geometry_msgs.msg import PoseStamped
from tf.transformations import quaternion_from_euler

parser = argparse.ArgumentParser(description='Send a Goal Position to a TB')
parser.add_argument('bot', metavar='BOT', type=str, help='Bot number (0,1,2)')
parser.add_argument('X', type=float, help="X Pos")
parser.add_argument('Y', type=float, help="Y Pos")
parser.add_argument('A', type=float, help="Angle (radians)")

args = parser.parse_args()

rospy.init_node('init_pos')
pub = rospy.Publisher('/tb3_' + args.bot + '/move_base_simple/goal', PoseStamped, queue_size = 10)
rospy.sleep(1)
checkpoint = PoseStamped()

checkpoint.pose.position.x = args.X
checkpoint.pose.position.y = args.Y
checkpoint.pose.position.z = 0.0

[x,y,z,w]=quaternion_from_euler(0.0,0.0,args.A)
checkpoint.pose.orientation.x = x
checkpoint.pose.orientation.y = y
checkpoint.pose.orientation.z = z
checkpoint.pose.orientation.w = w

checkpoint.header.frame_id = "map"

print(checkpoint)
pub.publish(checkpoint)