#!/usr/bin/python2
import time
import socket
import thread

send = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


while(True):
	def send():
		msg = input("Enter the msg...")
		msg = msg.encode()
	
		# msg to receiver
		send.sendto(msg,("127.0.0.1",9999))
		#time.sleep(1)
	def reply():
	
		#reply from receiver
		reply = send.recvfrom(1000)
		print reply[0].decode()
		#time.sleep(2)

thread.start_new_thread(send,())
thread.start_new_thread(reply,())

while True:
	pass
