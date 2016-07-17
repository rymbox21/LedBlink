import RPi.GPIO as GPIO
import time

#Set output pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)

while True: 
	try:
		n = int (input ("Blink count: "))
		a = 0
		if n >= 1:							#Negative number check		
			while  a != n:
				GPIO.output(13, GPIO.HIGH) 	#Set LED ON
				time.sleep (1)				#Delay for 1 sec
				GPIO.output(13, GPIO.LOW)	#Set LED OFF
				time.sleep (1)				#Delay for 1 sec
				a = a + 1
				print (a, end='\r')
			print()
			
		else:
			print("Invalid number")
	#Invalid input check		
	except ValueError:
		print("Invalid input")