#!/usr/bin/python3
from subprocess import call


string = input("Enter something!!")
path = call('echo $PATH')


print(path)
dat = call('cal')
print(dat)
