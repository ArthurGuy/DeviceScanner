
print("performing inquiry...")

from os import kill
import signal
import subprocess
import threading
import tempfile
import sys
import time
from tempfile import TemporaryFile
import commands
t = TemporaryFile()
global pipe_output
print commands.getoutput("hcitool dev")
print 'down'
commands.getoutput('hciconfig hci0 down')
print 'up'
commands.getoutput('hciconfig hci0 up')
print commands.getoutput("hcitool dev")
commands.getoutput('killall hcitool')
p = subprocess.Popen('hcitool lescan', bufsize = 0,shell = True, stdout =subprocess.PIPE,stderr = subprocess.STDOUT)
time.sleep(10)
#os.kill(p.pid,signal.SIGTERM)
for i in range(0,30,1):
    print 'for'
    inchar = p.stdout.readline()
    i+=1
    if inchar:
        print 'loop num:',i
        print str(inchar)
        t.write(str(inchar))
print 'out of loop'
t.seek(0)
print t.read()
