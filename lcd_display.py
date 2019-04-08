import RPi.GPIO as GPIO
import time 
# Define GPIO to LCD mapping
LCD_RS = 21
LCD_E  = 20
LCD_D4 = 26
LCD_D5 = 19
LCD_D6 = 13
LCD_D7 = 6
 
# Define some device constants
LCD_WIDTH = 20    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False
 
LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xD0 # LCD RAM address for the 2nd line
LCD_LINE_4 = 0xD8 # LCD RAM address for the 4th line
 
# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005
 
def main():
  # Main program block
 
  GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
  GPIO.setup(LCD_E, GPIO.OUT)  # E
  GPIO.setup(LCD_RS, GPIO.OUT) # RS
  GPIO.setup(LCD_D4, GPIO.OUT) # DB4
  GPIO.setup(LCD_D5, GPIO.OUT) # DB5
  GPIO.setup(LCD_D6, GPIO.OUT) # DB6
  GPIO.setup(LCD_D7, GPIO.OUT) # DB7

  GPIO.setup(2,GPIO.IN) #Light1 pin
  GPIO.setup(3,GPIO.IN) #Light2 pin
  GPIO.setup(10,GPIO.IN) #Fan pin

 
  # Initialise display
  lcd_init()
 
  while True:
    l1=GPIO.input(2)
    l2=GPIO.input(3)
    f=GPIO.input(10)
    print(l1,l2,f)
    #print the status of appliances
    if(l1==1 and l2==0 and f==0):
     lcd_string("LIGHT 1 ON",LCD_LINE_1,1)
     lcd_string("LIGHT 2 OFF",LCD_LINE_2,1)
     lcd_string("FAN     OFF",LCD_LINE_4,1)
    if(l1==0 and l2==1 and f==0):
     lcd_string("LIGHT 1 OFF",LCD_LINE_1,1)
     lcd_string("LIGHT 2 ON",LCD_LINE_2,1)
     lcd_string("FAN     OFF",LCD_LINE_4,1)
    if(l1==1 and l2==1 and f==0):
     lcd_string("LIGHT 1 ON",LCD_LINE_1,1)
     lcd_string("LIGHT 2 ON",LCD_LINE_2,1)
     lcd_string("FAN     OFF",LCD_LINE_4,1)
    if(l1==0 and l2==0 and f==1):
     lcd_string("LIGHT 1 OFF",LCD_LINE_1,1)
     lcd_string("LIGHT 2 OFF",LCD_LINE_2,1)
     lcd_string("FAN     ON",LCD_LINE_4,1)
    if(l1==1 and l2==0 and f==1):
     lcd_string("LIGHT 1 ON",LCD_LINE_1,1)
     lcd_string("LIGHT 2 OFF",LCD_LINE_2,1)
     lcd_string("FAN     ON",LCD_LINE_4,1)
    if(l1==0 and l2==1 and f==1):
     lcd_string("LIGHT 1 OFF",LCD_LINE_1,1)
     lcd_string("LIGHT 2 ON",LCD_LINE_2,1)
     lcd_string("FAN     ON",LCD_LINE_4,1)
    if(l1==0 and l2==0 and f==0):
     lcd_string("LIGHT 1 OFF",LCD_LINE_1,1)
     lcd_string("LIGHT 2 OFF",LCD_LINE_2,1)
     lcd_string("FAN     OFF",LCD_LINE_4,1)
    if(l1==1 and l2==1 and f==1):
     lcd_string("LIGHT 1 ON",LCD_LINE_1,1)
     lcd_string("LIGHT 2 ON",LCD_LINE_2,1)
     lcd_string("FAN     ON",LCD_LINE_4,1)
    time.sleep(1) # 3 second delay
 
def lcd_init():
  # Initialise display
  lcd_byte(0x33,LCD_CMD) # 110011 Initialise
  lcd_byte(0x32,LCD_CMD) # 110010 Initialise
  lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
  lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
  lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
  lcd_byte(0x01,LCD_CMD) # 000001 Clear display
  time.sleep(E_DELAY)
 
def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = data
  # mode = True  for character
  #        False for command
 
  GPIO.output(LCD_RS, mode) # RS
 
  # High bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x10==0x10:
    GPIO.output(LCD_D4, True)
  if bits&0x20==0x20:
    GPIO.output(LCD_D5, True)
  if bits&0x40==0x40:
    GPIO.output(LCD_D6, True)
  if bits&0x80==0x80:
    GPIO.output(LCD_D7, True)
 
  # Toggle 'Enable' pin
  lcd_toggle_enable()
 
def lcd_toggle_enable():
  # Toggle enable
  time.sleep(E_DELAY)
  GPIO.output(LCD_E, True)
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, False)
  time.sleep(E_DELAY)
 
def lcd_string(message,line,style):
  # Send string to display
  # style=1 Left justified
  # style=2 Centred
  # style=3 Right justified
 
  if style==1:
    message = message.ljust(LCD_WIDTH," ")
  elif style==2:
    message = message.center(LCD_WIDTH," ")
  elif style==3:
    message = message.rjust(LCD_WIDTH," ")
 
  lcd_byte(line, LCD_CMD)
 
  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)
 
if __name__ == '__main__':
 
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    lcd_byte(0x01, LCD_CMD)
    lcd_string("Goodbye!",LCD_LINE_1,1)
    GPIO.cleanup()

