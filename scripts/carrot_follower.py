#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from opencv_apps.msg import BlobArrayStamped

class CarrotFollower:

    def __init__(self):
        self.new_blob_available = False
        self.x_coord = 320
        self.size = 150
        self.timestamp = 0
        self.state = "locating"

        self.pub = rospy.Publisher("cmd_vel", Twist, queue_size=1)
        self.loop_rate = rospy.Rate(30)
        self.vel_msg = Twist()

        rospy.Subscriber("blobs", BlobArrayStamped, self.get_blob)

        self.main_loop()

    def get_blob(self, blob_msg):
        if len(blob_msg.blobs) > 0:
            self.new_blob_available = True
            self.x_coord = blob_msg.blobs[0].center.x
            self.size = blob_msg.blobs[0].radius
            self.timestamp = blob_msg.header.stamp.secs

    def main_loop(self):
        while not rospy.is_shutdown():
            if self.state == "locating":
                self.vel_msg.angular.z = 0.5
                self.vel_msg.linear.x = 0
                self.pub.publish(self.vel_msg)

                if self.new_blob_available:
                    self.new_blob_available = False
                    if self.x_coord < 120:
                        self.state = "approaching"

            if self.state == "approaching":
                if self.new_blob_available:
                    self.vel_msg.angular.z = (320 - self.x_coord) * 0.005
                    self.vel_msg.linear.x = (150 - self.size) * 0.002
                    self.pub.publish(self.vel_msg)
                    self.new_blob_available = False

                    if abs(320 - self.x_coord) < 10 and self.size > 145:
                        self.state = "locating"

                if rospy.get_time() - self.timestamp > 5:
                    self.state == "locating"

            self.loop_rate.sleep()

if __name__ == "__main__":
    rospy.init_node("carrot_follower")
    CarrotFollower()
