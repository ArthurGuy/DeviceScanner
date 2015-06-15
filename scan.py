import subprocess
import tempfile
import time
import os

#Reset Bluetooth interface, hci0
os.system("sudo hciconfig hci0 down")
os.system("sudo hciconfig hci0 up")

print("performing scan...")

from subprocess import Popen, PIPE

proc = Popen(["sudo timeout 20 hcitool lescan"], stdout=PIPE, bufsize=1) # start process

with p.stdout:
    for line in iter(p.stdout.readline, b''):
        print line,
p.wait() # wait for the subprocess to exit

print "Exit status", proc.returncode
