import sys
import Adafruit_DHT
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(10,GPIO.OUT) #pin for FAN
while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 8)
    print(temperature, humidity)
    if(temperature>27.0):
     GPIO.output(10,1)
    else:
     GPIO.output(10,0)
    time.sleep(1)
