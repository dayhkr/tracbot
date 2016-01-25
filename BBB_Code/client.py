#! /usr/bin/env python
"""
Trac bot main program communicates over i2c bus to
Aruduino microcontroller
"""

import getch
import socket
import sys

def senddata(message):
    try:
        message = 'This is the message.  It will be repeated.'
        print >>sys.stderr, 'sending "%s"' % message
        sock.sendall(message)

        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print >>sys.stderr, 'received "%s"' % data


def main():
    while(True):
        direction = getch.getch()
        if(direction == 'w'):
            senddata(1)
        elif(direction == 'a'):
            senddata(2)
        elif(direction == 's'):
            senddata(3)
        elif(direction == 'd'):
            senddata(4)
        elif(direction == 'f'):
            senddata(5)
        elif(direction == 'x'):
            sock.close()
            return
        else:
            print "Bad direction"

if __name__=="__main__":
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port on the server given by the caller
    server_address = ('192.168.1.193', 1337)
    print >>sys.stderr, 'connecting to %s port %s' % server_address
    sock.connect(server_address)
    main()

