#!/usr/bin/env python
import rospy
import cv2
from sensor_msgs.msg import Image 
from cv_bridge import CvBridge

def img_pub(msg):
    try:
        pub = rospy.Publisher('image_color', Image, queue_size=10)
        pub.publish(msg)
    except Exception as err:
        print err

def start_node():
    rospy.init_node('pub')
    rospy.Subscriber("image_raw", Image, img_pub)
    rospy.spin()
    
if __name__ == '__main__':
    try:
        start_node()
    except rospy.ROSInterruptException: 
        pass