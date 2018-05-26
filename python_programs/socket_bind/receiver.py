#!/usr/bin/python3

import socket,time
import numpy as np
import matplotlib.pyplot as plt

#code for reciever
rec_ip="127.0.0.1"
myport=8888

list_data = []
unique_element_list = []
variables = []
counting_element = []
count = 0
entered = 0
list_element_with_count = []
tuple_element = ()
list_variables = [["",[]]]
literals = []
count_data = []
list_element = []

first_time = 0
not_first_time = 0
l2 = []
element = []
l1=[]



#                 ipv4       ,  for UDP   
#   only  for rec                      
#  below method with argument creating a socket called  s 
r=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#  now connecting ip  and port 
r.bind((rec_ip,myport)) 
#  buffer size 

while 4 >  2 :
	#print(r.recvfrom(1000))
	data = r.recvfrom(1000)
	#print("data==>",data[0].decode())
	#print("Ip==>",data[1])		
	
	string = data[0].decode()
	#data_received = data[0].decode().strip().split()
	

	## as list formed already has the feature of strip and split so no need to write it again else list is formed inside list ##
	#data_received = data[0].decode()
	data_received = string.strip().split()

	count+=1

	for i in range(0,len(data_received)):
		list_data.append(data_received[i])
	

	if(count == 10):
		if(not_first_time == 0):
			first_time = 1
		else:
			first_time = 0
		entered = 1	
		
		count = 0 ## for the next iteration of data reception

		not_first_time = 1 
		
		variables.append(list_data[0])
		
		for i in range(0,len(list_data)):			
			if list_data[i] in variables:
				print("no unique element till now")
			else:
				variables.append(list_data[i])
					

	#if first_time == 1:
	for i in variables:
		list_variables.append([i,[list_data.count(i)]])
	
	
	length = len(list_variables)
	'''else:
		for i in variables:
			length = len(list_variables)
			for j in range(1,length-1):
				if i == list_variables[j][0]:
					list_variables[j][1].append(list_data.count(i))
					break

				elif i != list_variables[j][0]:
					list_variables.append([i,[list_data.count(i)]])
					break'''
			
	

	for i in range(1,len(list_variables)):
		plt.scatter(list_variables[i][0],list_variables[i][1],color='r')
	plt.show()
	time.sleep(2)
	

	if entered == 1:			
		list_data = []
		variables = []
		entered = 0	
		list_variables = [["",[]]]




	

	




					
