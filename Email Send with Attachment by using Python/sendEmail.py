import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def sendMail(emailVar,subjectVar,MessageVar,filename):
    email_sender='gaganaggarwal121@gmail.com'
    email_password='Enter Email Password Here'
    email_receiver=emailVar

    subject=subjectVar

    msg=MIMEMultipart()
    msg['From']=email_sender
    msg['To']=email_receiver
    msg['Subject']=subject

    message = MessageVar

    msg.attach(MIMEText(message,'plain'))

    FILE = filename # Any Format of file attached

    attachment=open(FILE,'rb')

    part=MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition','attachment; filename= '+FILE)
    msg.attach(part)
    text=msg.as_string()

    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_sender,email_password)
    server.sendmail(email_sender,email_receiver,text)
    server.quit()