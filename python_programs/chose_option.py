#! /usr/bin/python3

import urllib.request as ur
import time
#from google import search
#import google
import search_google
import os
import sys
from sys import platform
import requests
import re
from bs4 import BeautifulSoup
## library to query a website ##
import webbrowser
#import urllib2
import urllib

print ("Press1 : {Enter anything to get related website}")
print ("Press2 : {Enter anything to get related images}")
print ("Press3 : {Enter anything to get related URL of webpages}")
print ("Press4 : {to get current date and time}")
print ("Press5 : {to open default WebBrowser}")
print ("Press6 : {to check current connected IPs}")
print ("Press7 : {Enter domain and get owner's name and contact}")

## using python3 so instead of raw_input() use input() as raw_input() not works here ##
option = int(input())

if option == 1:
	print ("option 1 choosen,corresponding output is:")
	print ("Enter the string")
	str = input()
	list = str.split()
	## search for every keyword that is obtained in the splitted list ##
	for i in list:
	## function to open new tab for each searched keyword ##
		webbrowser.open_new_tab('https://www.google.com/search?q='+i)

elif option == 2:
	print ("option 2 choosen,corresponding output is:")
	print ("Enter the string")
	str = input()
	list = str.split()

	for i in list:
		webbrowser.open_new_tab("https://www.google.com/search?biw=1301&bih=670&tbm=isch&sa=1&ei=Fjn9WtLjLpD6rQGigqH4Ag&q="+i)

elif option == 3:
	print ("option 3 choosen,corresponding output is:")
	print ("Enter the string")
	str = input()
	list = str.strip().split()
	#fetch data using urllib.request and beautifulsoup libraries
	'''for i in list:
		url_from_web = webbrowser.open_new_tab("https://api.hackertarget.com/pagelinks/?q=https://www.google.com/search?q="+i)		
		print(url_from_web)
		#page = requests.get(url_from_web)
		#soup = Beautifulsoup(page.txt,'html.parser')'''
	page = ur.urlopen("http://"+str).read()
	#soup = BeautifulSoup(page)
	soup=BeautifulSoup(page,'lxml')
	soup.prettify()
	for anchor in soup.findAll('a', href=True):
	    print(anchor['href'])		
	
		
elif option == 4:
	print ("option 4 choosen,corresponding output is:")
	
	current_time = time.ctime()
	print (current_time)

elif option == 5:
	print ("option 5 choosen,corresponding output is:")
	if platform == "linux" or platform == "linux2":
		print("current operating system is :linux")
		url = "https://www.mozilla.org/en-US/firefox/central/"
		webbrowser.open(url)
	elif platform == "darwin":
		print("current operating system is: darwin")
		print("the default browser is:safari")
	elif platform == "win32":
		print("current operating system is : windows")
		print("default browser is Internet Explorer")

elif option == 6:
	print ("option 6 choosen,corresponding output is:")


elif option == 7:
	print ("option 7 choosen,corresponding output is:\n")
	str = input("Enter the domain_name for which you want to know the owners details     ")
	list_str = str.split()
	url = "https://en.wikipedia.org/wiki/"+str
	webbrowser.open(url)

else:
	print ("Choose a valid option")

