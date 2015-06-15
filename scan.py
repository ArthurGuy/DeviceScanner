from subprocess import Popen, PIPE, STDOUT

print("performing scan...")

proc = Popen(["sudo", "timeout", "20", "hcitool", "lescan"], stdout=PIPE, stderr=STDOUT, shell=True)
(device, err) = proc.communicate()

#Print bluetooth devices
print device

print err;

print "Exit status", proc.returncode
