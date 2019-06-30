#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import rospkg
from sound_system.srv import StringService, HotwordService, NLPService
from std_msgs.msg import String
import subprocess


class Load:

    def __init__(self):

        rospy.init_node("mapping_load")

        self.load_map_pub = rospy.Publisher("/navigation/load_location", String, queue_size=10)
        path = "{}/shell/{}".format(rospkg.RosPack().get_path("mapping"), "load.sh")
        command = ["bash", path, "map.yaml"]
        print(path, command)
        rospy.sleep(0.5)

        subprocess.Popen(command)
        file = rospy.get_param("{}/info_file".format(rospy.get_name()))
        self.load_map_pub.publish(file)


if __name__ == '__main__':
    Load()
