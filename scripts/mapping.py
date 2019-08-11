#!/usr/bin/env python
# -*- coding: utf-8 -*-
from location.srv import RegisterLocation
import rospy
from sound_system.srv import HotwordService, StringService
from std_msgs.msg import String


class Mapping:
    def __init__(self):
        self.register_topic = "/location/register_current_location"
        
        rospy.init_node("mapping")
        rospy.Subscriber("/mapping/register_place", String, self.register_callback)
        self.save_map_pub = rospy.Publisher("/location/save_location", String, queue_size=10)
        rospy.Subscriber("/sound_system/result", String, self.sound_callback)
        self.follow_me_control_pub = rospy.Publisher("/follow_me/control", String, queue_size=10)
    
    @staticmethod
    def hot_word():
        """
        「hey, ducker」に反応
        :return:
        """
        rospy.wait_for_service("/sound_system/hotword", timeout=1)
        print "hot_word待機"
        rospy.ServiceProxy("/sound_system/hotword", HotwordService)()
    
    def register_callback(self, msg):
        # type:(String)->None
        print "register"
        if not msg.data == "0":
            try:
                rospy.wait_for_service(self.register_topic, timeout=1)
                rospy.ServiceProxy(self.register_topic, RegisterLocation)(msg.data)
                print "登録しました。"
            except rospy.ROSException:
                print "Error, not find location node."
        else:
            self.save_map_pub.publish("mapping")
            print "セーブ"
    
    def sound_callback(self, msg):
        # type:(String)->None
        if msg.data == "follow me":
            self.follow_me_control_pub.publish('start')
        else:
            self.follow_me_control_pub.publish('stop')
    
    def main(self):
        while not rospy.is_shutdown():
            self.hot_word()
            rospy.ServiceProxy("/sound_system/recognition", StringService)("follow_me_sphinx")  # 音声認識開始


if __name__ == '__main__':
    mapping = Mapping()
    mapping.main()
