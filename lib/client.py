
import zmq
import os
from datetime import datetime
import sys
context = zmq.Context()

# open and read patch
infile = open(sys.argv[1],"r")
lines = infile.readlines()

all_lines = ""
for ln in lines:
    all_lines = all_lines + ln

size = str(os.fstat(infile.fileno())[6])

#size  = str(len(infile))

#  Socket to talk to server
socket = context.socket(zmq.REQ)
socket.connect ("tcp://192.168.1.68:5555")

# iterate over lines and send to server
#for line in lines:
    #    socket.send ("This is request number " + str(t.timeit())+ str(t.timeit()))
print "\nSending " + size + " bytes > Server at " + str(datetime.now())

socket.send (all_lines)
print " sent >"
#  Get the reply.
returned_sha = socket.recv()
print " < received " + str(returned_sha) + "\n"
os.system("git log | head -1 > patch/head_sha")
infile = open("patch/head_sha","r")
head_sha = infile.readline().split(' ',2) [1]
if head_sha == returned_sha:
    print "Repos synced"
    os.remove(sys.argv[1])
else:
    print "ERROR! Repos out of sync"

infile.close()
  #   print "Received reply "
 #       print ("message sent")
















