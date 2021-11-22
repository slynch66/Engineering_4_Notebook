# RPi GPIO Pin Intro

# Written by Sean Lynch

# 11.18.21

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM) #this sets my pin numbering scheme as BCM

GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW)
while True:
	GPIO.output(21, GPIO.HIGH)
	GPIO.output(20, GPIO.LOW)
	print("red on, blue off")
	sleep(1)
	GPIO.output(21, GPIO.LOW)
	GPIO.output(20, GPIO.HIGH)
	print("red off, blue on")
	sleep(1)
