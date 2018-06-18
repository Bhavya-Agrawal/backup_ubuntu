#!/usr/bin/python3

import re
import dns.resolver
import socket
import smtplib

#addressToVerify ='bhavya19agrawal@gmail.com'
addressToVerify ='bhavyaagarwal.cse19@jecrc.ac.in'
match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)
try:
	if match == None:
		print('Bad Syntax')
		raise ValueError('Bad Syntax')
	else:
		print("a good mail syntax")

except ValueError:
	print("not a valid mail id")		



# to check validity of the email
records = dns.resolver.query('google.com', 'MX')
mxRecord = records[0].exchange
mxRecord = str(mxRecord)	




# to check if the sender email address exists or not (not checks for if the receivers mail address exists or not),if it exists this will return true for code==250  and prints success else it will return false and prints Bad,check by changing the sender mail address to check 
# Get local server hostname
host = socket.gethostname()
print(host)

# SMTP lib setup (use debug level for full output)
server = smtplib.SMTP()
server.set_debuglevel(0)

# SMTP Conversation
server.connect(mxRecord)
server.helo(host)
server.mail('bhavya19agrawal@gmail.com')
code, message = server.rcpt(str(addressToVerify))
print("code,message:  ",code,message)
server.quit()

# Assume 250 as Success
if code == 250:
	print('Success')
else:
	print('Bad')
