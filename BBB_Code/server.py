import socket
import sys
from thread import *
#import smbus

DEVICE_ADDRESS = 0x08
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 1337 # Arbitrary non-privileged port
running = 1
#def sendCmd(data):

    #bus = smbus.SMBus(1)
    #bus.write_byte(DEVICE_ADDRESS, data)

#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client
    conn.send('Tracbot v0.1 Control channel\n') #send only takes string
     
    #infinite loop so that function do not terminate and thread do not end.
    while True:
        reply = ''
        #Receiving from client
        data = conn.recv(1024)
        if data:
            reply = '<ACK>' + data + "<ACK>"
            print data
            data = data.strip()
            if data == "5":
                #reply = '<ACK>' + data + "<ACK>"
                break
            elif data == "6":
                print "yeah 6"
                #need to open comm back to main from thread
            else:
                #reply = '<ACK>' + data + "<ACK>"
                conn.send("Bad command")

            if reply:
                conn.send(reply)
    conn.close()

def main(s):
    #now keep talking with the client

    while running == 1:
        #wait to accept a connection - blocking call
        conn, addr = s.accept()
        print 'Connected with ' + addr[0] + ':' + str(addr[1])
     
        #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
        start_new_thread(clientthread ,(conn,))
 
    s.close()

if __name__=="__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print 'Socket created'

    #Bind socket to local host and port
    try:
        s.bind((HOST, PORT))
    except socket.error as msg:
        print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()

    print 'Socket bind complete'

    #Start listening on socket
    s.listen(10)
    print 'Socket now listening'
    main(s)