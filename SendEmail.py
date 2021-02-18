#imports
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import sys

def readFile(filePath):
    with open(filePath, 'r') as f:
        return f.read()

#login
usr = readFile('./user.txt')
pwd = readFile('./progPass.txt')

#sendMessage using To, subject, and message
def sendMessage(toAddr, Subj, Message, Count):
    #Build message using mime
    msg = MIMEMultipart()
    msg['From'] = usr
    msg['To'] = toAddr
    msg['Subject'] = Subj 

    msg.attach(MIMEText(Message, 'plain'))

    #Setup server and login
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(usr, pwd)

    #Send email, then close
    for i in range(0, Count):
        server.send_message(msg, usr, toAddr)
        print("Sent " + str(i+1))
    server.close()

sendMessage(sys.argv[1],sys.argv[2],sys.argv[3],int(sys.argv[4]))