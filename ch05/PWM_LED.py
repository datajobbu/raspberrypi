#-*- coding: utf-
import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)
p = GPIO.PWM(18, 50) # pin 18 - 50Hz

p.start(0)

try:
	while True:
		for dc in range(0, 101, 5):
			p.ChangeDutyCycle(dc)
			time.sleep(0.3)
		
		for dc in range(100, -1, -5):
			p.ChangeDutyCycle(dc)
			time.sleep(0.3)
except KeyboardInterrupt:
	pass
	
p.stop()
GPIO.cleanup()
