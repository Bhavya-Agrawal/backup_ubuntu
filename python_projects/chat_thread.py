#!/usr/bin/python2
import time
import socket
#import threading
import thread

def sender():

	send = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


	while(True):
		#msg = input("Enter the msg...")
		msg = raw_input("Enter the msg!!!!!      ")		
		msg = msg.encode()
	
		# msg to receiver
		send.sendto(msg,("127.0.0.1",9999))
		#reply from receiver
		reply = send.recvfrom(1000)
		print reply[0].decode()
		time.sleep(1)      

 
def receiver():

	rec = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	#sender doesn't need to bind only the receiver need to bind as initially only 1 is the receiver,second one gets the reply as a receiver

	# to connect publically enter public IP here find via whatismyip

	rec.bind(("127.0.0.1",9999))

	while(True):
		# msg from sender
		data = rec.recvfrom(1000)
		#data[0].decode()
		print data[0].decode()
		# data contains a list of 2 dimension 1st is msg from sender 2nd is tuple of(IP,Socket of sender)
		
		msg = raw_input("Enter the reply!!!!!     ")
		msg.encode()
		#msg = input("Enter your reply...").encode()
		#msg = msg.encode() reply to sender
		rec.sendto(msg,(data[1]))
		time.sleep(1)


# first call sender by thread then receiver
thread.start_new_thread(sender,())
thread.start_new_thread(receiver,())


#to keep thread progressing after 1st call also
while True:
	pass

