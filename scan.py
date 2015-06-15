from subprocess import Popen, PIPE, STDOUT

print("performing scan...")

proc = Popen(["sudo", "hcitool", "lescan"], stdout=PIPE, bufsize=1, stderr=STDOUT, close_fds=True) # start process
for line in iter(proc.stdout.readline, b''): # read output line-by-line
    print line,

proc.stdout.close()
proc.wait()

#proc.communicate() # close `proc.stdout`, wait for child process to terminate
print "Exit status", proc.returncode
