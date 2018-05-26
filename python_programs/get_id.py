

#!/usr/bin/python

import gc

print "Enter at random 2 values"

a=raw_input()
b=raw_input()

print "id(a)==>"+str(id(a))

print "id(b)==>"+str(id(b))

#print type(id(a))
print "Enter the id for which you want to find an allocated object"
id_ = int(raw_input())

def ob_by_id(idd_):
	idd_ = id_

		## for searching object in the system ##
	#for obj in gc.get_objects():
	for obj in globals().values():

		if id(obj) == idd_:
			print "returned obj is " + obj
			break	

			#return obj

		else:
			print "No object found"
			break	
	

id_1 = ob_by_id(id_)
id_1

