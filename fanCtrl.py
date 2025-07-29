#!/bin/python3

import os
from time import sleep
import RPi.GPIO as GPIO

from signal import pause

fanPin = 21

desiredTemp = 45
period = 10

fanCtrl = None

minSpeed = 25
fanSpeed = 50
sum = 0
pTemp = 15
iTemp = 0.4

def getTemp():
	temp = os.popen("cat /sys/class/thermal/thermal_zone0/temp").readline()
	return int(temp) / 1000

def handleFan():
	global fanCtrl, fanSpeed, sum, minSpeed
	diff = getTemp() - desiredTemp
	sum += diff
	pdiff = diff * pTemp
	idiff = sum * iTemp
	fanSpeed = pdiff + idiff
	if fanSpeed > 100:
		fanSpeed = 100
	if fanSpeed < minSpeed:
		fanSpeed = 0
	if sum > 100:
		sum = 100
	if sum < 100:
		sum = -100
	#print("fan:", fanSpeed, "cur diff:", diff, "sum:", sum, "pdiff:", pdiff, "idff:", idiff)
	if fanCtrl:
		fanCtrl.ChangeDutyCycle(fanSpeed)


if __name__ == "__main__":
	print("initial temp:", getTemp(), "C")

	try:
		print("setting mode")
		GPIO.setmode(GPIO.BCM)
		print("setting pin")
		GPIO.setup(fanPin, GPIO.OUT)
		print("setting PWM")
		fanCtrl = GPIO.PWM(fanPin, 50)
		print("starting")
		fanCtrl.start(fanSpeed)	#15 is basically 0, 100 is max
		#pause()
		while True:
			handleFan()
			sleep(period)
	except Exception as e:
		print(e)
		print("cleaning up")
		if fanCtrl:
			fanCtrl.ChangeDutyCycle(0)
			fanCtrl.stop()
		GPIO.cleanup()
		print("done")
