import subprocess
import tempfile
import time
import os
import json
import requests

url = "http://requestb.in/v6s4jmv6"

print("performing scan...")

#Reset Bluetooth interface
os.system("sudo hciconfig hci0 down")
os.system("sudo hciconfig hci0 up")

#Start the scan
os.system("sudo hcitool lescan > results.txt &")

#wait for the results
time.sleep(20)

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

print len(results), "devices found"

print results

device_list = []

#Split into mac and name
for result in results:
    result_parts = result.split(" ", 1)
    device_list.append({'mac': result_parts[0], 'name': result_parts[1]})
#results = [s.split(" ", 1) for s in results]

print device_list

print json.dumps(device_list)

r = requests.post(url, data=json.dumps(device_list))
