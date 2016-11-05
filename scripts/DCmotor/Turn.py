#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

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

################################# DC motor test!
myMotor1 = mh.getMotor(1)
myMotor2 = mh.getMotor(2)
myMotor3 = mh.getMotor(3)
myMotor4 = mh.getMotor(4)

# set the speed to start, from 0 (off) to 255 (max speed)
myMotor1.setSpeed(150)
myMotor2.setSpeed(150)
myMotor3.setSpeed(150)
myMotor4.setSpeed(150)
 
myMotor1.run(Adafruit_MotorHAT.FORWARD);
myMotor2.run(Adafruit_MotorHAT.FORWARD);
myMotor3.run(Adafruit_MotorHAT.FORWARD);
myMotor4.run(Adafruit_MotorHAT.FORWARD);
# turn on motor
myMotor1.run(Adafruit_MotorHAT.RELEASE);
myMotor2.run(Adafruit_MotorHAT.RELEASE);
myMotor3.run(Adafruit_MotorHAT.RELEASE);
myMotor4.run(Adafruit_MotorHAT.RELEASE);

#parse command line arguments
numargs = len(sys.argv)

if(numargs > 0):
	#for the sake of ease, strictly enforcing syntax: script dir( 'right' || 'left' ) degrees( int )
	direction = sys.argv[1]
	degrees = int(sys.argv[2])

# Run the motor
if(direction == 'right'):
	myMotor1.run(Adafruit_MotorHAT.FORWARD)
	myMotor2.run(Adafruit_MotorHAT.FORWARD)
	myMotor3.run(Adafruit_MotorHAT.BACKWARD)
	myMotor4.run(Adafruit_MotorHAT.BACKWARD)
else:
	myMotor1.run(Adafruit_MotorHAT.BACKWARD)
	myMotor2.run(Adafruit_MotorHAT.BACKWARD)
	myMotor3.run(Adafruit_MotorHAT.FORWARD)
	myMotor4.run(Adafruit_MotorHAT.FORWARD)

myMotor1.setSpeed(250)
myMotor2.setSpeed(250)
myMotor3.setSpeed(250)
myMotor4.setSpeed(250)
time.sleep(1.0)

# Stop the motor
myMotor1.setSpeed(0)
myMotor2.setSpeed(0)
myMotor3.setSpeed(0)
myMotor4.setSpeed(0)