#!/usr/bin/python
# Display the IP Address of the RPI Device
from time import sleep

try: 
	import RPi.GPIO as GPIO
except RuntimeError:
	print("Error importing RPi.GPIO!")

def set_gpio():
	OW_PIN = 7
	GPIO.setmode(GPIO.BOARD)
	
def gpio_mode():
	print ("GPIO Mode: " + GPIO.getmode())
	return GPIO.getmode()

def ow_reset():
	GPIO.setup(OW_PIN, GPIO.OUT)
	GPIO.output(OW_PIN, false) #pull low
	sleep(0.05)
	GPIO.output(OW_PIN, true)
	
	GPIO.setup(OW_PIN, GPIO.IN)	
	sleep(0.01) 
	
	return GPIO.input(OW_PIN)
	
def 