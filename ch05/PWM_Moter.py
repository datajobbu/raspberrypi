#-*- coding: utf-
import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)

p = GPIO.PWM(18, 50) # pin 18 - 100Hz
p.start(0)

try:
	while True:
		p.ChangeDutyCycle(7.5)
		time.sleep(1)
		p.ChangeDutyCycle(12.5)
		time.sleep(1)
		p.ChangeDutyCycle(2.5)
		time.sleep(1)
		
except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()
