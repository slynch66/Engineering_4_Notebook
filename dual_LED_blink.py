# RPi GPIO Pin Intro

# Written by Sean Lynch

# 11.18.21

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM) #this sets my pin numbering scheme as BCM

GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)  #this sets pin 20 and 21 as outputs, and sets the output to no power
GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW)
# This while loop makes the LEDs alternate between red and blue being on
while True:
	GPIO.output(21, GPIO.HIGH)
	GPIO.output(20, GPIO.LOW)
	print("red on, blue off")
	sleep(1)                         # wait one full second
	GPIO.output(21, GPIO.LOW)
	GPIO.output(20, GPIO.HIGH)
	print("red off, blue on")
	sleep(1)                         # wait one full second
