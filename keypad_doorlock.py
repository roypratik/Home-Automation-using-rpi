import RPi.GPIO as GPIO
import time
from pad4pi import rpi_gpio
import requests
alarm= 9
servoPIN =23
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setup(alarm, GPIO.OUT)
GPIO.output(alarm,False)
p = GPIO.PWM(servoPIN, 50) # GPIO 23 for PWM with 50Hz
p.start(2.5) # Initialization
# Setup Keypad
KEYPAD = [
        ["1","2","3","A"],
        ["4","5","6","B"],
        ["7","8","9","C"],
        ["*","0","#","D"]
]
print("Enter the code")
a=[]
b=[1,4,5,7]
i=0
# same as calling: factory.create_4_by_4_keypad, still we put here fyi:
COL_PINS = [17,15,14,4] # BCM numbering
ROW_PINS = [24,22,27,18] # BCM numbering

GPIO.setup(17,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
factory = rpi_gpio.KeypadFactory()

# Try factory.create_4_by_3_keypad
# and factory.create_4_by_4_keypad for reasonable defaults
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)

#keypad.cleanup()
def check(a):
    global i
    if(a==b):
     print("Door Unlocked")
     print(a,i)
     r=requests.post("https://maker.ifttt.com/trigger/door_open/with/key/authkey")
     p.ChangeDutyCycle(10)
     time.sleep(5)
     p.ChangeDutyCycle(2.5)
     i=0
     return
    if(a!=b and i!=2):
     print("Wrong Key")
     print(str(2-i)+" Chances Remaining")
     i+=1
     print(a,i)
     return
    if(a!=b and i==2):
     print("Alarm Raised")
     print(a,i)
     r=requests.post("https://maker.ifttt.com/trigger/Alarm_raised/with/key/authkey")
     GPIO.output(alarm, True)
     while(True):
      print("Alarm")
      time.sleep(5)

def printKey(key):
    global a
    a.append(int(key))
    print(key)
    if(len(a)==4):
     check(a)
     a=[]

# printKey will be called each time a keypad button is pressed
keypad.registerKeyPressHandler(printKey)

try:
  while(True):
    time.sleep(0.2)
except:
 keypad.cleanup()
