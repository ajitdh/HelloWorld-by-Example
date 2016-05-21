#! /usr/bin/env python3
#  -*- coding:utf-8 -*-

# lines above this line are necessary
# use hash for comment
# touch helloworld.py -> to create the file
# python3 helloworld.py -> to run this helloworld example
# def __init__ is for constructor

# time.sleep(1)
import time 

#datetime.datetime.now()
import datetime

class HelloWorldClass:
	def __init__(self):
		self._title = 'Hello' 		
	
	def helloWorldMethod(self, name='World'):
		self._time = datetime.datetime.now().time()
		print(self._title  + ' ' + self._title + ' ' + name)
		 

#=== FUN ===
helloWorldClass = HelloWorldClass()

try:
	while True:
		helloWorldClass.helloWorldMethod()
		helloWorldClass.helloWorldMethod('MyName')		
		time.sleep(1)

except KeyboardInterrupt:
	pass
