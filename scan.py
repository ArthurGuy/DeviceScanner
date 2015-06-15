from subprocess import Popen, PIPE, STDOUT
import os


#Reset Bluetooth interface, hci0
os.system("sudo hciconfig hci0 down")
os.system("sudo hciconfig hci0 up")


print("performing scan...")

proc = Popen(["sudo timeout 20 hcitool lescan"], stdout=PIPE, shell=True)
(device, err) = proc.communicate()

#Print bluetooth devices
print device

print err;

print "Exit status", proc.returncode
