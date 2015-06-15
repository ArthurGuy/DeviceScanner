import subprocess
import tempfile
import time
import os

#Reset Bluetooth interface, hci0
os.system("sudo hciconfig hci0 down")
os.system("sudo hciconfig hci0 up")

print("performing scan...")

from subprocess import Popen, PIPE

proc = Popen(["sudo", "hcitool", "lescan"], stdout=PIPE, bufsize=1) # start process

time.sleep(20)

proc.terminate()

for line in iter(proc.stdout.readline, b''): # read output line-by-line
    print line,
# reached EOF, nothing more to read
proc.communicate() # close `proc.stdout`, wait for child process to terminate
print "Exit status", proc.returncode
