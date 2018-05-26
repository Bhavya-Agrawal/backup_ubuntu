#!/usr/bin/env   python

#import numpy as np
import socket
import time
import thread
import os


rec_ip="192.168.10.76"  # use of the receiver ip or ip 127.0.0.1
port=8888   # this no should be > 6000

            #ipv4        UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# create a socket argument s

s.bind((rec_ip,port))

def send():
    while 1:
        data_msg=raw_input("")
        s.sendto(data_msg,('192.168.10.22',port))


def rec():
    while 1:
        y = s.recvfrom(1000)
        print y[0]
        os.system('espeak')

thread.start_new_thread(send,())
thread.start_new_thread(rec,())

while 1:
    pass
