
import zmq
import os
from datetime import datetime
import sys
context = zmq.Context()

# open and read patch
#infile = open(sys.argv[1],"r")

infile = open("bundle/bundle.bundle","rb")
incontents = infile.read()
size = str(os.fstat(infile.fileno())[6])
infile.close()

#size  = str(len(infile))

#  Socket to talk to server
socket = context.socket(zmq.REQ)
socket.connect ("tcp://192.168.1.68:5555")

# iterate over lines and send to server
#for line in lines:
    #    socket.send ("This is request number " + str(t.timeit())+ str(t.timeit()))
print "\nSending " + size + " bytes > Server at " + str(datetime.now())

socket.send (incontents)
print " sent >"
#  Get the reply.
returned_sha = socket.recv()
print " < received " + str(returned_sha) + "\n"
os.system("git log | head -1 > patch/head_sha")
outfile = open("patch/remote_sha","w")
outfile.write(returned_sha)
outfile.close()

infile = open("patch/head_sha","r")
head_sha = infile.readline().split(' ',2) [1]
infile.close()
if head_sha == returned_sha:
    print "Repos synced Ok"
#    os.remove(sys.argv[1])
else:
    print "ERROR! Repos out of sync"
  #   print "Received reply "
 #       print ("message sent")
















