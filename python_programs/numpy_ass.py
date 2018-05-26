#!/usr/bin/python3

##run this file as python3 file_name

import numpy as np

global count
count = 0	#for counting no of inputs
valid_input = 1		#for getting inputs until q is reached
print("enter the values and press q: to stop as any further input")

even=0
user_input = input()

list_elements=[]	#to check count of no of elements entered
list_factors=[]		#to keep count of no of factors 
list_elements.append(user_input)

## to compare strings in python function used is str1.equals(str2)  ##

while valid_input != 0:
	if user_input != "q":
		user_input = input()
		if user_input != "q":
			list_elements.append(user_input)		
		count+=1

	else:
		break

print("list formed==>"+str(list_elements))
print("count==>"+str(count))

def count_factors(count1):
	count_no = count1
	global count				##for declaring global variables##
	global even
	for i in range(2,count_no//2+1):
		if count%i==0:
			print ("matrix can be formed from them")
			l1=count//i
			if i in list_factors and l1 in list_factors:
				print("nothing to be added else in factors list")
			else:
				list_factors.append(i)
				list_factors.append(l1)
				list_factors.append(l1)
				list_factors.append(i)
				even = 1	

		elif(i==count_no//2 and even!=1):
			print("enter one more number")
			user_input = input()
			list_elements.append(user_input)
			count+=1	
			list_factors.append(2)
			list_factors.append(count//2)
			list_factors.append(count//2)
			list_factors.append(2)
			counter = count_factors(count)
			counter
		else:
			continue
			


counter = count_factors(count)
counter

		
print("list_factors==>"+str(list_factors))
print(" you have entered "+str(count)+" elements ")
print ("enter the prefered size of the matrix you want from the input")
row = int(input())
column = int(input())

length = len(list_factors)

if row in list_factors:
	row1 = row
	column1 = count//row1
	np1=np.array(list_elements)
	print(np1.reshape(row1,column1))

else:
	if (row*column == count and (row!=1 or column!=1) and (row!=0 or column!=0)):	
		print ("matrix can be formed with this size")
		np1=np.array(list_elements)
		print(np1.reshape(row1,column1))
	else:
		print("sorry not a valid size for forming the matrix with the given input of size count")
		np1=np.array(list_elements)
		print(np1.reshape(row1,column1))


## to search item at a specific location in list use method listname.index(element)
