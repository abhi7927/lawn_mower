import RPi.GPIO as GPIO
#from app import val 

GPIO.setmode(GPIO.BCM)

LED = 18

GPIO.setup(LED,GPIO.OUT)
val = True
if val:
    GPIO.output(LED, GPIO.LOW)
    
