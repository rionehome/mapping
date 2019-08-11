#!/usr/bin/env python
# -*- coding: utf-8 -*-
from location.srv import RegisterLocation
import rospy
from std_msgs.msg import String


class Mapping:
    def __init__(self):
        self.register_topic = "/location/register_current_location"

        rospy.init_node("mapping")
        self.save_map_pub = rospy.Publisher("/location/save_location", String, queue_size=10)

        self.main()

    def main(self):
        while True:
            word = raw_input("place: ")
            if not word == "0":
                try:
                    rospy.wait_for_service(self.register_topic, timeout=1)
                    rospy.ServiceProxy(self.register_topic, RegisterLocation)(word)
                except rospy.ROSException:
                    print "Error, not find location node."
            else:
                self.save_map_pub.publish("mapping")
                print "セーブ"


if __name__ == '__main__':
    Mapping()
    rospy.spin()
