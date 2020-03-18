import os
import sys
import socket

acceptor = socket.socket()
acceptor.bind(('localhost', 8000))
acceptor.listen(10)

for i in range(3):
    pid = os.fork()
    
    if pid == 0:
        childpid = os.getpid()
        try:
            while 1:
                conn, addr = acceptor.accept()
                flo = conn.makefile()
                flo.write('Child %s echo> ' % childpid)
                flo.flush()
                message = flo.readline()
                flo.write(message)
                conn.close()
        except KeyboardInterrupt:
            sys.exit()

try:
    os.waitpid(-1, 0)
except KeyboardInterrupt:
    print("Done")
    sys.exit()