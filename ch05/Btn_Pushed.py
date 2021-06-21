import RPi.GPIO as GPIO
import time


button_pin = 15

def button_callback(channel):
	print("Button Pushed!")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(button_pin, GPIO.RISING, callback=button_callback)

while True:
	time.sleep(0.1)

