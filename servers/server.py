import sys
sys.path.append('/home/athira/Desktop/test16/DNN_chatbot/')
from engine import response
import chatbot_config as cfg
import socket               # Import socket module
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = cfg.port                # Reserve a port for your service.
print (host,port)
s.bind((host, port))        # Bind to the port
print("----------------Server Running---------------")
s.listen(cfg.n_connection)                 # Now wait for client connection.
c, addr = s.accept()     # Establish connection with client.
print ('Got connection from', addr)
while True:
    print("All ok")
    q=c.recv(1024)
    #c=s.accept()
    a=q.decode('ascii')
    a=str(response(str(a)))
    print(a)
    c.send(a.encode('ascii'))
c.close() 
