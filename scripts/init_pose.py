#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from nav_msgs.msg import Odometry

# node initialization
# this gives initial pose to the nav stack and then tries to align both the static 
# and physical map together
rospy.init_node('init_pose')
# poseWithCovarianceStamped is needed to manipulate the /InitialPose topic
# publish on behave of Rviz to make sure it is aligned with gazebo
pub = rospy.Publisher('/initialpose', PoseWithCovarianceStamped, queue_size = 1)

# construct message

init_msg = PoseWithCovarianceStamped()
# mimic Rviz (rostopic echo /initialPose)
init_msg.header.frame_id = "map"

# pass the right initial pose to amcl 
# get initial pose from Gazebo
# odom gives the position of the robot relative to the gazebo env
# copy odoms location to the init_msg
odom_msg = rospy.wait_for_message('/odom', Odometry)
init_msg.pose.pose.position.x = odom_msg.pose.pose.position.x
init_msg.pose.pose.position.y = odom_msg.pose.pose.position.y
init_msg.pose.pose.position.z = odom_msg.pose.pose.position.z
init_msg.pose.pose.orientation.x = odom_msg.pose.pose.orientation.x
init_msg.pose.pose.orientation.y = odom_msg.pose.pose.orientation.y
init_msg.pose.pose.orientation.z = odom_msg.pose.pose.orientation.z
init_msg.pose.pose.orientation.w = odom_msg.pose.pose.orientation.w

# time allow set pose
rospy.sleep(1)

# Publish message
rospy.loginfo("setting initial pose")
pub.publish(init_msg)
rospy.loginfo("initial pose is set")
