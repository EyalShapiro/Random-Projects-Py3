from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
mail_content = """
Hello,Eyal —— erg97ghbuyregf9h
Thank You
"""
# The mail addresses and password
sender_address = 'send@outlgpb.8'  # מייל השולח'
sender_pass = 'pass'  # password from sender_address
receiver_address = 'getting@gmail.com'  # מייל הנשלח
# Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
# The subject line
message['Subject'] = 'A test mail sent by Python. It has an attachment.'
# The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
# Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(sender_address, sender_pass)
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')
