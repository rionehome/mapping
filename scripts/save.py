#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import rospkg
from sound_system.srv import StringService, HotwordService, NLPService
from std_msgs.msg import String
import subprocess


class Save:

    def __init__(self):
        rospy.init_node("mapping_save")
        self.save_map_pub = rospy.Publisher("/navigation/save_location", String, queue_size=10)
        rospy.sleep(0.5)
        path = "{}/shell/{}".format(rospkg.RosPack().get_path('mapping'), "save.sh")
        command = ["bash", path]
        subprocess.Popen(command)
        self.save_map_pub.publish("mapping")


if __name__ == '__main__':
    Save()
