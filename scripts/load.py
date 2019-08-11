#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import rospkg
from std_msgs.msg import String
import subprocess


class Load:
    def __init__(self):

        rospy.init_node("mapping_load")

        self.load_map_pub = rospy.Publisher("/location/load_location", String, queue_size=10)
        path = "{}/shell/{}".format(rospkg.RosPack().get_path("mapping"), "load.sh")
        command = ["bash", path, "map.yaml"]

        # gmappingが立ち上がってからでないと初期化されてしまうのでgmappingが立ち上がるまで待機
        rospy.sleep(2.0)

        subprocess.Popen(command)
        file_name = rospy.get_param("{}/info_file".format(rospy.get_name()))
        self.load_map_pub.publish(file_name)


if __name__ == '__main__':
    Load()
