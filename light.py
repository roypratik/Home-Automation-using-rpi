import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.IN) #Read output from light sensor
GPIO.setup(3, GPIO.OUT)         #Light2 output pin
GPIO.setup(2,GPIO.OUT)           #LIGHT 1
GPIO.setup(10,GPIO.OUT)           #Fan
while True:
 i=GPIO.input(25)
 print(i)
 if(i==0):                 #When output from LIGHT  sensor is LOW
  GPIO.output(3, 0)  #Turn OFF Lights
  GPIO.output(2,0)
  time.sleep(0.1)
 elif i==1:               #When output from LIGHT sensor is HIGH
  GPIO.output(3, 1)  #Turn ON Lights
  GPIO.output(2,1)
  time.sleep(0.1)





