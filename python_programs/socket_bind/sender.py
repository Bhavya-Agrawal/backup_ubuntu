import socket
import time


#    code for sender
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


while True:
	msg = input("enter the msg:")  ## or msg = input("enter the msg:").encode() 
	s.sendto(msg.encode(),("127.0.0.1",8888))




# use msg.encode('utf-8') or msg.encode() 
	
