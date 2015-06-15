import subprocess
import tempfile
import time
import os

print("performing scan...")

#Reset Bluetooth interface
os.system("sudo hciconfig hci0 down")
os.system("sudo hciconfig hci0 up")

#Start the scan
os.system("sudo hcitool lescan > results.txt &")

#wait for the results
time.sleep(10)

#Stop the scan
os.system("sudo pkill --signal SIGINT hcitool")

#Move the results file into a list
f = open('results.txt', 'r')
results = f.readlines()
f.closed

#Remove empty lines from the list
results = filter(None, results)

print results
