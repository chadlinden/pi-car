#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit
import sys

class Unit:
	def __init__(self):
		self.mh = Adafruit_MotorHAT(addr=0x60)
		self.motors = {}
		self.setup()

	def setup():
		self.motors['fr'] = self.mh.getMotor(1)
		self.motors['br'] = self.mh.getMotor(2)
		self.motors['fl'] = self.mh.getMotor(3)
		self.motors['bl'] = self.mh.getMotor(4)