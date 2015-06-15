from subprocess import Popen, PIPE, STDOUT

print("performing scan...")

proc = Popen(["sudo", "timeout", "20", "hcitool", "lescan"], stdout=PIPE, bufsize=1, stderr=STDOUT, close_fds=True) # start process
(device, err) = proc.communicate()

#Print bluetooth devices
print device


print "Exit status", proc.returncode
