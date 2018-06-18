#!/usr/bin/python3

# stop the security of mail Id running www.google.com/lesssecureapps

import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)

#to start service
server.starttls()

#logging in
server.login("bhavya19agrawal@gmail.com","Bhavya1910")

#send mail
msg = "hello!! demo mail by smtp via python3 file not terminal"
server.sendmail("bhavya19agrawal@gmail.com","bhavyaagarwal.cse19@jecrc.ac.in",msg)

