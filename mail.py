import smtplib

#Can't be named 'email.py'
#This is really simple, I just have it here as I tend to reuse this code

#Creds
from_address = '?'
username = '?'
password = '?'
server = 'smtp.gmail.com:587'

def email(recipient, message, subject):
    global username
    global password
    global from_address
    global server
    message = 'Subject: %s\n\n%s' % (subject, message)
    server = smtplib.SMTP(server)
    server.starttls()
    server.login(username,password)
    server.sendmail(from_address, recipient, message)
    server.quit()

email('maildotpy@wfc.help', 'test', 'test')
