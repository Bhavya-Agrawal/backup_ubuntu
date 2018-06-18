#!/usr/bin/python
import smtplib
import time
import imaplib
import email

# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------
ORG_EMAIL   = "@gmail.com"
username = raw_input("enter username eg abc\n")
FROM_EMAIL  = username + ORG_EMAIL
print("FROM_EMAIL:  ",FROM_EMAIL)
yourPassword = raw_input("enter the password for the mail adress\n")
FROM_PWD    = yourPassword
print("FROM_PWD:  ",FROM_PWD)
# to read incoming mail use "imap" for sending mail use "smtp.gmail.com"
SMTP_SERVER = "imap.gmail.com"
# port no of smtp is 25 and for imap is 993
SMTP_PORT   = 993

def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()   
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])


        for i in range(latest_email_id,first_email_id, -1):
            typ, data = mail.fetch(i, '(RFC822)' )

            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1])
                    email_subject = msg['subject']
                    email_from = msg['from']
                    print 'From : ' + email_from + '\n'
                    print 'Subject : ' + email_subject + '\n'

    except Exception, e:
        print str(e)

if __name__ == "__main__":
    read_email_from_gmail()        