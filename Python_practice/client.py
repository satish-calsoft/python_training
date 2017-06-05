#!/usr/bin/python           # This is client.py file

import socket,threading # Import socket module

##def send():
##    
##    while True:
##        
##        msg = raw_input('\nMe Clent> ')
##        s.send(msg)
##
##def receive():
##    while True:
##        #sen_name = c.recv(1024)
##        data = s.recv(1024)
##
##        print('\n' + "Server::" + ' > ' + str(data))
        
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
host = socket.gethostname() # Get local machine name

port = 12343              # Reserve a port for your service.

s.connect((host, port))


while True:
    msg = raw_input("Enter message:")
    if msg:

        s.send(msg)
    data = s.recv(1024)
    print "received:",data


##threading.Thread(target = receive).start()
##threading.Thread(target = send).start()

