# imports
import zmq
import os
from datetime import datetime
import sys

# create context

context = zmq.Context(1)

# open and read patch

infile = open("bundle/bundle.bundle","rb")
incontents = infile.read()
size = str(os.fstat(infile.fileno())[6])
infile.close()

#  create socket to talk to server

socket = context.socket(zmq.REQ)
socket.connect ("tcp://192.168.1.66:5555")

# Send bundle to server

print "\nSending " + size + " bytes > Server at " + str(datetime.now())
socket.send (incontents)
print " sent >"

#  Get reply.from server

returned_sha = socket.recv()
print " < received " + str(returned_sha) + "\n"

# write to log to screen

os.system("git log | head -1 > patch/head_sha")

# write remote_sha to file

outfile = open("patch/remote_sha","w")
outfile.write(returned_sha)
outfile.close()

# read head sha from file

infile = open("patch/head_sha","r")
head_sha = infile.readline().split(' ',2) [1]
infile.close()

# verify local and remote shas are the same and report

if head_sha == returned_sha:
    print "Repos synced Ok"
else:
    print "ERROR! Repos out of sync"
















