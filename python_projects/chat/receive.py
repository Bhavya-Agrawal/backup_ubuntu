#!/usr/bin/python2
import time
import socket


rec = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
rec.bind(("127.0.0.1",9999))

while(True):
	
	# msg from sender
	data = rec.recvfrom(1000)
	#data[0].decode()
	print(data[0].decode())
	#time.sleep(1)

	
	# data contains a list of 2 dimension 1st is msg from sender 2nd is tuple of(IP,Socket of sender)
	msg = input("Enter your reply...").encode()
	#	msg = msg.encode() reply to sender
	rec.sendto(msg,(data[1]))
	#time.sleep(2)



