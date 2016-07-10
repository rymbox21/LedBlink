import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(13, GPIO.OUT)

n = int (input ("Blink count: "))
a = 0

while a != n:
	GPIO.output(13, GPIO.HIGH)
	time.sleep (0.125)
	GPIO.output(13, GPIO.LOW)
	time.sleep (0.125)
	a = a + 1
	print (a, end='\r')
print ()
	
