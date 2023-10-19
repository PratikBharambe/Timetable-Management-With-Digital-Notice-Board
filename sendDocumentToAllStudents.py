import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

import numpy as np
import pandas as pd

df = pd.read_csv('studdata.csv')
# Access the data in the desired column using the column name
email_of_student = df['Email']

# Convert the data to a NumPy array for further processing

mail_Address = np.array(email_of_student)

# Set up SMTP server credentials
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'bharambepratik2002@gmail.com'
smtp_password = ''

# Set up the email message
msg = MIMEMultipart()
msg['From'] = smtp_username
msg['To'] = ", ".join(mail_Address)
msg['Subject'] = 'Mails For Students'

# Attach the document to the email
with open('rmd.jpeg', 'rb') as f:
    attachment = MIMEApplication(f.read(), _subtype='pdf')
    attachment.add_header('Content-Disposition', 'attachment', filename='rmd.jpeg')
    msg.attach(attachment)

# Connect to the SMTP server and send the email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(smtp_username, mail_Address, msg.as_string())
