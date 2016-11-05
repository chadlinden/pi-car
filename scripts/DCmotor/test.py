#!/usr/bin/python
from forward import DCmotor


# assign a motor
print "Assign motor 1"
myMotor = DCmotor(1)

# motor should run for 255*0.01 seconds forward
print "Run for 255*0.01 second"
myMotor.go(255, 1)  