import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(3, GPIO.OUT)         #Light2 output pin
GPIO.setup(2,GPIO.OUT)           #LIGHT 1
GPIO.setup(10,GPIO.OUT)           #Fan
while True:
 j=GPIO.input(11)
 print(j)
 if(j==0):                 #When output from PIR is LOW
  GPIO.output(3, 0)  #Turn OFF Lights
  GPIO.output(2,0)
  time.sleep(0.1)
 elif j==1:               #When output from PIR sensor is HIGH
  GPIO.output(3, 1)  #Turn ON Lights
  GPIO.output(2,1)
  time.sleep(0.1)


