#!/usr/bin/python           # This is server.py file

import socket,threading               # Import socket module
from select import select

##def send():
##    while True:
##        
##        msg = raw_input('\nMe Server> ')
##        c.send(msg)
##
##def receive():
##    while True:
##        #sen_name = c.recv(1024)
##        data = c.recv(1024)
##
##        print('\n' + "Client::" + ' > ' + str(data))
        

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12005             # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
#s.setblocking(0)
print "Listening...."
s.listen(5)             # Now wait for client connection.

c, addr = s.accept()     # Establish connection with client.
print addr

print 'Got connection from', addr

    
while True:
    data = c.recv(1024)
    send_message(src,dest, data)
    print "received:",data


##    reply = raw_input("reply:")
##    c.sendall(reply)

##threading.Thread(target = send).start()
##threading.Thread(target = receive).start()
##
