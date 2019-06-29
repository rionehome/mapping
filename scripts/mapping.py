#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from sound_system.srv import StringService, HotwordService, NLPService
from std_msgs.msg import String


class Mapping:
	def __init__(self):
		self.change_dict_pub = rospy.Publisher("/sound_system/sphinx/dict", String, queue_size=10)
		self.change_gram_pub = rospy.Publisher("/sound_system/sphinx/gram", String, queue_size=10)
		
		self.main()
	
	def resume_text(self, dict_name):
		# type: (str)->str
		"""
		音声認識
		:return:
		"""
		self.change_dict_pub.publish(dict_name + ".dict")
		self.change_gram_pub.publish(dict_name + ".gram")
		rospy.wait_for_service("/sound_system/recognition")
		response = rospy.ServiceProxy("/sound_system/recognition", StringService)()
		return response.response
	
	@staticmethod
	def hot_word():
		"""
		「hey, ducker」に反応
		:return:
		"""
		rospy.wait_for_service("/hotword/detect", timeout=1)
		print "hot_word待機"
		rospy.ServiceProxy("/hotword/detect", HotwordService)()
	
	@staticmethod
	def speak(sentence):
		# type: (str) -> None
		"""
		peak関数
		:param sentence:
		:return:
		"""
		rospy.wait_for_service("/sound_system/speak")
		rospy.ServiceProxy("/sound_system/speak", StringService)(sentence)
	
	def main(self):
		while True:
			rospy.wait_for_service('/sound_system/nlp', timeout=1)
			print rospy.ServiceProxy('/sound_system/nlp', NLPService)('Here is {}'.format(raw_input("place: ")))


if __name__ == '__main__':
	Mapping()
	rospy.spin()
