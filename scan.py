import subprocess
import tempfile
import time
import os

#Reset Bluetooth interface, hci0
os.system("sudo hciconfig hci0 down")
os.system("sudo hciconfig hci0 up")

print("performing scan...")

# open temporary file (it automatically deleted when it is closed)
    #  `Popen` requires `f.fileno()` so `SpooledTemporaryFile` adds nothing here
    f = tempfile.TemporaryFile() 

    # start process, redirect stdout
    p = subprocess.Popen(["sudo hcitool lescan"], stdout=f)

    # wait 2 seconds
    time.sleep(20)

    # kill process
    #NOTE: if it doesn't kill the process then `p.wait()` blocks forever
    p.terminate() 
    p.wait() # wait for the process to terminate otherwise the output is garbled

    # print saved output
    f.seek(0) # rewind to the beginning of the file
    print f.read(), 
    f.close()
