import hashlib
import server
import time

self_hash = False
do_exit   = False

# generate sha1 hash of file
def hash_file(file_path):
    sha1 = hashlib.sha1()
    f=open(file_path,"rb")
    try:
        sha1.update(f.read())
    finally:
        f.close()
    return sha1.hexdigest()

# main process

self_hash = hash_file("server.py")

while not do_exit:
    print "Starting Server\n"
    do_reload = False
    while not do_reload:
        server.zmq_serve()

    # if server has changed reload
        if self_hash != hash_file("server.py"):
            self_hash = hash_file("server.py")
            do_reload = True
    print "Stopping Server"
    time.sleep(0.2)

    reload(server)
