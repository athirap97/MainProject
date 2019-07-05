import socket               # Import socket module
import sys
s = socket.socket()         # Create a socket object
host = "athira-sys"  # Get local machine name
port = 1234                # Reserve a port for your service.
s.connect((host, port))
while True:
    #inp=raw_input("User: ")
    inp=input("User: ")
    s.send(inp.encode('ascii'))
    recv=s.recv(1024)
    print ("SCT_bot: ",recv.decode('ascii'))
    if recv=='stop':
        s.close
        sys.exit()
        break

s.shutdown(); s.close()
#s.close # Close the socket when done
