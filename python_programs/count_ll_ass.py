#! /usr/bin/python
print "take five inputs from the user"

t=()
for i in range(0,5):
	t=t+tuple(input())
print "t===== "+str(t)
#def count_ll_in_tuple(t1):
t1=t

for i in range(0,len(t1)):
	if isinstance(t1[i],str):		
		for j in range(0,len(t1[i])-1):
			if(t1[i][j]=='l' and t1[i][j+1]=='l'):
				print " ll is found in the tuple in "+t1[i]+" at position "+ str(j)	
			#elif isinstance(t1[i],tuple):
			#	count_ll_in_tuple(t1[i])
						
	else:
		print " No possible position of ll in " + str(i) + "input of the tuple"
	



#tuple_demo=count_ll_in_tuple(t)
#tuple_demo

#for(i=0;i<len(t);i++)     for making comments in python
