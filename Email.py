
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = "bmvengwa@gmail.com"
receiver_email = "bmvengwa@gmail.com"
subject = "Subject of the email"
body = "Body of the email"

# Create the MIME object
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Attach the body to the email
message.attach(MIMEText(body, "plain"))

# Connect to the SMTP server (Gmail example)
smtp_server = "smtp.gmail.com"
smtp_port = 587
username = "your email  username"
password = "your app name"

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(username, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
print("done")

