#!/usr/bin/python

import subprocess
import tempfile
import time
import os
import json
import requests

import math
import time
import socket, urllib2

import signal
import sys

import Adafruit_CharLCD as LCD

url = "https://bbms.buildbrighton.com/device-scanner"




# shutdown handler
def signal_handler(signal, frame):
    print 'Stopping...'
    # kill the bluetooth scan
    os.system("sudo pkill --signal SIGINT hcitool")
    print ' done'
    sys.exit(0)

# register the handler
signal.signal(signal.SIGINT, signal_handler)


# Initialize the LCD using the pins 
lcd = LCD.Adafruit_CharLCDPlate()

lcd.set_backlight(1)





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
		lcd.set_backlight(1)
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


# Display start message
lcd.clear()
lcd.message('Device Scanner')
time.sleep(3.0)

while True:

	# Display scan start message
	lcd.clear()
	lcd.message('Scanning...')
	
	print("performing scan...")
	
	#Reset Bluetooth interface
	os.system("sudo hciconfig hci0 down")
	os.system("sudo hciconfig hci0 up")
	
	#Start the scan
	os.system("sudo hcitool lescan > results.txt &")
	
	#wait for the results
	time.sleep(30)
	
	#Stop the scan
	os.system("sudo pkill --signal SIGINT hcitool")
	
	#Move the results file into a list
	f = open('results.txt', 'r')
	results = f.readlines()
	f.closed
	
	#Remove empty lines from the list
	results = filter(None, results)
	
	#trim each item - removes the newline character
	results = [s.strip() for s in results]
	
	#Remove the fist info message
	if "LE Scan ..." in results: results.remove("LE Scan ...")
	
	#process results
	
	device_list = {}
	
	#Split into mac and name
	for result in results:
	    result_parts = result.split(" ", 1)
	    mac = result_parts[0];
	    name = result_parts[1];
	    if (name == '(unknown)'):
	    	name = ''
	    
	    # if nac not set or max name is empty
	    if (not mac in device_list or not device_list[mac]):
	    	device_list[mac] = name
	
	print len(device_list), "devices found"
	
	# Output the number of devices found to the display
	lcd.clear()
	lcd.message(str(len(device_list)) + " devices found")
	lcd.message("Uploading");
	
	print device_list
	
	#print json.dumps(device_list)
	
	# Send the data to the server
	headers = {'content-type': 'application/json'}
	r = requests.post(url, data=json.dumps(device_list), headers=headers)
	
	lcd.clear()
	lcd.message(str(len(device_list)) + " devices found")
	lcd.message("Sleeping");

	# Wait 30 seconds and then do it again
	time.sleep(30)

