import collections
import subprocess
import threading
import os


#Reset Bluetooth interface, hci0
os.system("sudo hciconfig hci0 down")
os.system("sudo hciconfig hci0 up")


print("performing scan...")

#proc = Popen(["sudo timeout 20 hcitool lescan"], stdout=PIPE, shell=True)
# start process, redirect stdout
process = subprocess.Popen(["sudo hcitool lescan"], stdout=subprocess.PIPE)

# terminate process in timeout seconds
timeout = 20 # seconds
timer = threading.Timer(timeout, process.terminate)
timer.start()

# save last `number_of_lines` lines of the process output
number_of_lines = 20
q = collections.deque(process.stdout, maxlen=number_of_lines)
timer.cancel()

# print saved lines
print ''.join(q)
