#!/usr/bin/python3
import time
import socket

send = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


while(True):
	
	msg = input("Enter the msg...")
	msg = msg.encode()
	
	# msg to receiver
	send.sendto(msg,("127.0.0.1",9999))
	#time.sleep(1)
	
	
	#reply from receiver
	reply = send.recvfrom(1000)
	print(reply[0].decode())
	#time.sleep(2)


