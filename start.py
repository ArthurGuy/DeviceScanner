#!/usr/bin/python
# Example using a character LCD plate.
import math
import time
import socket, urllib2

import Adafruit_CharLCD as LCD


# Initialize the LCD using the pins 
lcd = LCD.Adafruit_CharLCDPlate()

lcd.backlight(lcd.ON)


'''
#WIP - startup on boot
def internetOn():
	try:
		response=urllib2.urlopen('http://google.com',timeout=3)
		return True
	except urllib2.URLError as err:
		pass
	return False
'''


#Check for network connection at startup
t = time.time()
while True:
	lcd.clear()
	lcd.message('checking network\nconnection ...')
	if (time.time() - t) > 120:
		# No connection reached after 2 minutes
		lcd.clear()
		lcd.message('network is\nunavailable')
		time.sleep(30)
		exit(0)
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(('8.8.8.8', 0))
		lcd.backlight(lcd.ON)
		lcd.clear()
		lcd.message('IP address:\n' + s.getsockname()[0])
		time.sleep(5)
		# display.initInfo()	# Start info gathering/display
		break         		# Success
	except:
		time.sleep(1) 		# Pause a moment, keep trying
'''
	if internetOn() == True:
		time.sleep(5)
		break         # Success
	else:
		time.sleep(1) # Pause a moment, keep trying
'''




# Show some basic colors.
lcd.clear()
lcd.message('Device Scanner')
time.sleep(3.0)


# Show button state.
lcd.clear()
lcd.message('Press buttons...')

# Make list of button value, text, and backlight color.
buttons = ( (LCD.SELECT, 'Select'),
            (LCD.LEFT,   'Left'),
            (LCD.UP,     'Up'),
            (LCD.DOWN,   'Down'),
            (LCD.RIGHT,  'Right') )

print 'Press Ctrl-C to quit.'
while True:
	# Loop through each button and check if it is pressed.
	for button in buttons:
		if lcd.is_pressed(button[0]):
			# Button is pressed, change the message and backlight.
			lcd.clear()
			lcd.message(button[1])

