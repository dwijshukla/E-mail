import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

send = "email address of SENDER"
rec = "email address of RECIEVER"

msg = MIMEMultipart()

#sorting sender and reciever
msg['From'] = send
msg['To'] = rec

msg['subject'] = "Enter Subject of Mail"
body = "body of mail"

msg.attach(MIMEText(body, 'plain'))

file_name = "file name with extension"
attachment = open("path of file", "rb")  #enter the path of file u want to send

p = MIMEBase('application', 'octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)

p.add_header('content-disposition', "attachment; filename = %s" % filename)
msg.attach(p)
s = smtplib.SMTP('smtp.gamil.com', 587)

s.starttls()
s.login(send, "password of sender")

text = msg.as_string()
s.sendmail(send, rec, text)

s.quit()

# if we want to send msg to many user you can use loop 
