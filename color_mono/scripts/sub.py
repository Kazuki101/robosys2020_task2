#!/usr/bin/env python
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def img_sub(msg):
    try:
        bridge = CvBridge()
        color = bridge.imgmsg_to_cv2(msg, "bgr8")
        gray = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)
        _, mono = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)

        cv2.imshow('color', color)
        cv2.imshow('gray', gray)
        cv2.imshow('mono', mono)
        cv2.waitKey(10)
    except Exception as err:
        print err

def start_node():
    rospy.init_node('sub')
    rospy.Subscriber("image_color", Image, img_sub)
    rospy.spin()

if __name__ == '__main__':
    try:
        start_node()
    except rospy.ROSInterruptException:
        pass
