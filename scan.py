import subprocess
import tempfile
import time
import os

#Reset Bluetooth interface, hci0
os.system("sudo hciconfig hci0 down")
os.system("sudo hciconfig hci0 up")

print("performing scan...")

//Start the scan
os.system("sudo hcitool lescan > results.txt &")

time.sleep(10)

//Stop the scan
os.system("sudo pkill --signal SIGINT hcitool")

with open('results.txt', 'r') as f:
    read_data = f.read()
    print read_data
f.closed
