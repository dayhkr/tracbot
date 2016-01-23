#! /usr/bin/env python
"""
Trac bot main program communicates over i2c bus to
Aruduino microcontroller
"""

import smbus
import time
import getch
import sys

DEVICE_ADDRESS = 0x08

def sendCmd(data):

    bus = smbus.SMBus(1)
    bus.write_byte(DEVICE_ADDRESS, data)

def remote():
    print "wasd and f to stop"
    while(True):
        direction = getch.getch()
        if(direction == 'w'):
            sendCmd(1)
        elif(direction == 'a'):
            sendCmd(2)
        elif(direction == 's'):
            sendCmd(3)
        elif(direction == 'd'):
            sendCmd(4)
        elif(direction == 'f'):
            sendCmd(5)
        elif(direction == 'x'):
            return
        else:
            print "Bad direction"
def auto():
    pass

def main():
    while(True):
        mode = raw_input("Enter 1 for remote 2 for autonomous any other key to exit: ")

        if mode == "1":
            remote()
        elif mode == "2":
            auto()
        else:
            sys.exit()

if __name__=="__main__":
    main()

