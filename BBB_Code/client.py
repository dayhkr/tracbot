#! /usr/bin/env python
"""
Trac bot main program communicates over i2c bus to
Aruduino microcontroller
"""

import getch
import socket
import sys

help = "w = forward\na = left\ns = backwards\nd = right\nf = stop\nx = disconnect\nh = help"


def senddata(message):
    try:
        print >>sys.stderr, 'sending "%s"' % message
        sock.sendall(message)

        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(1024)
            amount_received += len(data)
            print >>sys.stderr, 'received "%s"' % data
    except Exception as e:
        print e


def main():
    print "Press h for commands"
    while True:
        direction = getch.getch()
        if direction == 'w':
            senddata("1")
        elif direction == 'a':
            senddata("2")
        elif direction == 's':
            senddata("3")
        elif direction == 'd':
            senddata("4")
        elif direction == 'f':
            senddata("5")
        elif direction == 'x':
            senddata("6")
            sock.close()
            return
        elif direction == 'h':
            print help
        else:
            print "Bad direction"

if __name__ == "__main__":
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port on the server given by the caller
    server_address = ('192.168.1.193', 1337)
    print >>sys.stderr, 'connecting to %s port %s' % server_address
    sock.connect(server_address)
    data = sock.recv(1024)
    print >>sys.stderr, 'received "%s"' % data

    main()
