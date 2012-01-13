#   Binds REP socket to tcp://*:5555

import zmq
import os

context = zmq.Context()
socket = context.socket(zmq.REP)

socket.bind("tcp://*:5555")

def zmq_serve():
    message = socket.recv()
    os.system("clear")

#    print "Saving patch..."
#    outfile = open("patch/patch.patch", "w")
#    outfile.write(message)
#    print message + "\n\n"
#    outfile.close()
#    print "...patch saved"

    print "Saving bundle..."
    outfile = open("bundle/bundle.bundle", "w")
    outfile.write(message)
#    print message + "\n\n"
    outfile.close()
    os.remove("bundle/bundle.bundle")
    print "...patch saved"

    # apply patch
#    print "\nchecking commit..."
#    if not os.system("git apply --check < \"patch/patch.patch\"\n"):
#        print "...checked\napplying commit...\n"
#        os.system("git am --committer-date-is-author-date < \"patch/patch.patch\"\n")
#    else:
#        print "ERROR! Patch will not apply\n\n"

    os.system("git pull bundle/bundle.bundle master")
#    os.system("git unbundle")

#    os.system("git log -1 --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr)%Creset' --abbrev-commit --date=relative")
    os.system("\n\n")

    # return head sha
    os.system("git log | head -1 > patch/head_sha")
    infile = open("patch/head_sha","r")
    head_sha = infile.readline().split(' ',2) [1]
    infile.close()

    # send head sha as reply
    socket.send(str(head_sha))
