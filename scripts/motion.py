#!/usr/bin/python

# initiate motors and exit process
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import argparse
import time
import atexit
import sys
import math

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
parser.add_argument('--command', help='direction command (forward |BACKWARD)')
parser.add_argument('--speed', help='Speed (0-255)')
parser.add_argument('--moment', help='Seconds / 100 (0-255)')
parser.add_argument('--heading', help='Degrees (-90-+90')

args = parser.parse_args()


class Motion:
    def __init__(self, Adafruit_MotorHAT, Adafruit_DCMotor, args):
        self.mh = Adafruit_MotorHAT(addr=0x60)
        self.fr = mh.getMotor(1)
        self.br = mh.getMotor(2)
        self.fl = mh.getMotor(3)
        self.bl = mh.getMotor(4)
        self.run(args)

    def run(self, args):
        if( args.command == 'FORWARD'):
            self.fr.run(Adafruit_MotorHAT.FORWARD)
            self.br.run(Adafruit_MotorHAT.BACKWARD)
            self.fl.run(Adafruit_MotorHAT.BACKWARD)
            self.bl.run(Adafruit_MotorHAT.FORWARD)
        else:
            self.fr.run(Adafruit_MotorHAT.BACKWARD)
            self.br.run(Adafruit_MotorHAT.FORWARD)
            self.fl.run(Adafruit_MotorHAT.FORWARD)
            self.bl.run(Adafruit_MotorHAT.BACKWARD)

        self.motorSpeeds( int(args.speed), int(args.heading) )

        time.sleep(0.01 * float(args.moment))

        self.fl.setSpeed(0)
        self.bl.setSpeed(0)
        self.fr.setSpeed(0)
        self.br.setSpeed(0)

    def motorSpeeds(self, speed, heading):
        speed = int(speed)
        heading = int(heading)
        # speed - ( ( |heading| / 90 ) * speed )
        if(heading != 0):
            reduced = int( speed -  ( (math.fabs(heading) / 90 ) * speed) )
        else:
            reduced = speed
        if( heading > 0):
            #adjust right side
            self.fr.setSpeed(reduced)
            self.br.setSpeed(reduced)
            self.fl.setSpeed( args.speed )
            self.bl.setSpeed( args.speed )
        else:
            self.fr.setSpeed( args.speed )
            self.br.setSpeed( args.speed )
            self.fl.setSpeed(reduced)
            self.bl.setSpeed(reduced)
        print("speed:"+str(speed)+"reduced:"+str(reduced)+"heading:"+str(heading))

motor = Adafruit_DCMotor
run = Motion(Adafruit_MotorHAT, Adafruit_DCMotor, args)






