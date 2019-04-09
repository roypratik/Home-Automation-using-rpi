# Home-Automation-using-rpi
A simple home automation project using raspberry pi 3 Model B.
There are 3 parts in this project.

          1. Home Appliances Control using Blynk library and app.

          2. LCD status display of the appliances in real time.

          3. Keypad Lock with status notification on phone using IFttt.

          4. Automated home appliances control.
 
 Part 1
 
 The rpi is directly connected to a four channel relay module that is connected to two LEDs representing two lights and a DC motor with wheel representing the ceiling fan. The Blynk library is used to interface with the mobile app of Blynk with which the appliances are controlled real time.
 
 Part 2
 
  A 16x4 LCD display has been used for the status of the appliances, interfaced with the Rpi. The display is real time and as soon the status is toggled from the Blynk app, the display gets updated.
	
 Part 3
 
 The door lock representing the front door of an house is being represented by a servo motor. A 4x4 keypad lock is being used to automate the whole system.The system is interfaced with ifttt and as soon as the door is opened upon correct code, a notifiaction will be sent to the user's cell phone. Upon entering wrong code for thrice an alarm will be reaised using a buzzer and a notification will also be sent at the same time. The system won't accept the right code after the alarm is raised until it as been reset. The change in duty cycle of the servo motor represents the unlocking and locking of the door lock.
 
 Part 4
 
The automated system in which enviromental factors controls the appliances. 
The sensors used are DHT11, PIR sensor and LIGHT sensor. When the temperature of the room is greater than a certain value then the DC motor that represents a ceiling fan automatically turns on. The Light sensor senses amount of lighting in the environment and automatically controls the lighting system of the room. The PIR sensor detects motion and automatically switches the lights of the room on.
