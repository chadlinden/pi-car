#!/usr/bin/python

# initiate motors and exit process
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import argparse
import time
import atexit
import sys

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)


# initiate CLI parser
parser = argparse.ArgumentParser(description='Control robot motions.')
parser.add_argument('--command', help='direction command (forward |reverse)')
parser.add_argument('--speed', help='Speed (0-255)')
parser.add_argument('--moment', help='Seconds / 100 (0-255)')

args = parser.parse_args()
print(args)

class Motion:
    def __init__(self, Adafruit_MotorHAT, Adafruit_DCMotor, args):
        self.mh = Adafruit_MotorHAT(addr=0x60)
        self.fr = mh.getMotor(1).run(Adafruit_MotorHAT.FORWARD)
        self.fl = mh.getMotor(2).run(Adafruit_MotorHAT.FORWARD)
        self.br = mh.getMotor(3).run(Adafruit_MotorHAT.FORWARD)
        self.bl = mh.getMotor(4).run(Adafruit_MotorHAT.FORWARD)

