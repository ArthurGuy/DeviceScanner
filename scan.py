from subprocess import Popen, PIPE

print("performing scan...")

proc = Popen(["sudo", "hcitool", "lescan"], stdout=PIPE, bufsize=1) # start process
for line in iter(proc.stdout.readline, b''): # read output line-by-line
    print line,
# reached EOF, nothing more to read
proc.communicate() # close `proc.stdout`, wait for child process to terminate
print "Exit status", proc.returncode
