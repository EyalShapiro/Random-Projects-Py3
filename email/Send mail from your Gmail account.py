from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

MAIL_CONTENT = """
Hello,Eyal —— erg97ghbuyregf9h
Thank You
"""
# The mail addresses and password
SENDER_ADDRESS = "send@outlgpb.8"
SENDER_PASS = "pass"  # password from sender_address
RECEIVER_ADDRESS = "getting@gmail.com"


if __name__ == "__main__":
    # Setup the MIME
    message = MIMEMultipart()
    message["From"] = SENDER_ADDRESS
    message["To"] = RECEIVER_ADDRESS
    # The subject line
    message["Subject"] = "A test mail sent by Python. It has an attachment."
    # The body and the attachments for the mail
    message.attach(MIMEText(MAIL_CONTENT, "plain"))
    # Create SMTP session for sending the mail
    session = smtplib.SMTP("smtp.gmail.com", 587)
    session.starttls()
    session.login(SENDER_ADDRESS, SENDER_PASS)
    text = message.as_string()
    session.sendmail(SENDER_ADDRESS, RECEIVER_ADDRESS, text)
    session.quit()
    print("Mail Sent")
