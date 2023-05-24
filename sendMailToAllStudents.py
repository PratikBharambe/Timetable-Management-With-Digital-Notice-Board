import datetime
import time

from email.message import EmailMessage
import ssl
import smtplib

import numpy as np
import pandas as pd

df = pd.read_csv('studdata.csv')
# Access the data in the desired column using the column name
email_of_student = df['Email']

# Convert the data to a NumPy array for further processing
mail_Address = np.array(email_of_student)


def sendMail(email_receiver, body):

    try:
        email_sender = "bharambepratik2002@gmail.com"
        email_password = "yhexjdsegqiforwq"

        subject = "Sending mail using python"

        em = EmailMessage()

        em["From"] = email_sender
        em["To"] = ", ".join(email_receiver)
        em["Subject"] = subject
        em.set_content(body)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
            return
    except:
        print("NoInternetConnectionError_PleaseCheckInternetConnection")

msg = "You are getting this mail from Python for testing purpose !!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

while True:
    now = datetime.datetime.now()
    if now.hour == 10 and now.minute == 36:
        sendMail(mail_Address, msg)
        break
    else:
        print(now)
        time.sleep(5)
