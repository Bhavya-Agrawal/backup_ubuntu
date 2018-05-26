#! /usr/bin/python
print "take five inputs from the user"
t=()
for k in range(0,5):
	t=t+tuple(input())

print "tuple formed====>"+str(t)
tuple_count=0
count=0

print count

def count_ll_in_tuple(t1):
	#tuple_count_1=tuple_count
	for i in range(0,len(t1)):

		if isinstance(t1[i],str):
		
			for j in range(0,len(t1[i])-1):

				if(t1[i][j]=='l' and t1[i][j+1]=='l'):
					#print "ll is found in the tuple in tuple no in input "+str(i)+" at position "+ str(j)
					print "ll is found in the tuple in input "+str(t1[i])+"at position"+ str(j)
				#elif(t1[i][j]=='l' and t1[i][j+1]=='l' and count==1):
				#	print " ll is found in the tuple in "+t1[i]+" at position "+ str(j)
					
				#length=length-1				#this condition is out of all if statement as its in correspondence to for 					
		elif isinstance(t1[i],tuple):
			#count=1
			#tuple_count_1=tuple_count_1+1
			count_ll_in_tuple(t1[i])
			#length=length-1

		else:
				#print " ll is not present in the input "+str(i)+" of tuple_no "+str(touple_count)
				print " ll is not present in the input "+str(t1[i])
				#length=length-1	


tuple_demo=count_ll_in_tuple(t)				#to call function definition like we do via main function in C,Java...
tuple_demo


