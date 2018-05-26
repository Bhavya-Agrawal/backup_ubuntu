#!/usr/bin/python3

from os import mkdir,rmdir
import sys
from pathlib import Path
import os

#fetching sorce and destination files from terminal
file_names = sys.argv[1:3]
not_exists = 0

#print(file_names)

#opening source_file in read mode
#source_file = file_names[0]

source_file = Path(file_names[0])
print(source_file)
#chech if sorce file exists or not
if source_file.is_file():
	f = open(source_file,'r')
	#reading data of sorce file
	data = f.read()
	f.close
	not_exists = 0

#sorce is a directory
elif source_file.is_dir():
	path = file_names[0]
	print("source_file  "+file_names[0]+"  is a directory" )
	for filename in os.listdir(path):
		print("Files present in the directory are  "+filename)	
	not_exists = 0	


else:
	print("the source file  "+file_names[0]+"  doesn't exists")
	not_exists = 1


if not_exists == 0:

#opening destination file in write mode
	destination_file = file_names[1]
	df = open(destination_file,'w')
	df.write(data)
	df.close()
else:
	pass
