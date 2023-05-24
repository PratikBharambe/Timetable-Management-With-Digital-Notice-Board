
#inporting all the necessary modules ......................
import imaplib
import time
from imapclient import IMAPClient
import email
import datetime

from email.message import EmailMessage
import ssl
import smtplib

import numpy as np
import pandas as pd

# Ids for rescheduling lectures accoring to current day ...............
mondayresheduleid = [4, 3]
tuesdayresheduleid = [4, 3]
wednesdayresheduleid = [2, 3]
thursdayresheduleid = [1, 2]
fridayresheduleid = [4, 1]

# Reading the tefaculty csv file and importing all the data ...............
df = pd.read_csv('tefaculty.csv')

# Access the data in the desired column using the column name ..............
Faculty_ID = df["id"]
Faculty_name = df["name of faculty"]
Faculty_Mail = df["mail"]
Faculty_subject = df["subject"]

# Convert the data to a NumPy array for further processing .....................
faculty_id = np.array(Faculty_ID)
faculty_name = np.array(Faculty_name)
faculty_mail = np.array(Faculty_Mail)
faculty_subject = np.array(Faculty_subject)


# Generating a class to store dictionaries & boolean values ........................
class allVariablesAndDictionaries:
    is_resheduled = False
    resheduledDateAndTimeDict = {}

# object of the above call to access allt he variables and dictionaries ...............
VandD = allVariablesAndDictionaries()

# imap data for sending and getting data from gmail account .......................
imap_server = 'imap.gmail.com'
imap_username = 'bharambepratik2002@gmail.com'
imap_password = 'yhexjdsegqiforwq'


# function to send a mail to the faculty .......................
def sendMail(email_receiver, body):

    email_sender = imap_username
    email_password = imap_password
    now = datetime.datetime.now()
    if (now.hour == 9):
        subject = "Practical scheduled REMAINDER"
    else:
        subject = "Lecture scheduled REMAINDER"
    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_receiver
    em["Subject"] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        msg = em.as_string()
        smtp.sendmail(email_sender, email_receiver, msg)
        print("Mail sent to : ", email_receiver)
        print(body)


# function to get the time of the ;ast received mail on gmail account ........................
def getLastMailTime():
    # Connect to the email server .....................
    server = IMAPClient(imap_server, use_uid=True, ssl=True)
    server.login(imap_username, imap_password)

    # Select the mailbox/folder to fetch messages from ..............
    mailbox = 'INBOX'
    server.select_folder(mailbox)

    # Fetch the last received message and get the received time ......................
    messages = server.search(['ALL'])
    last_message_id = messages[-1]
    response = server.fetch(last_message_id, ['INTERNALDATE'])
    received_time = response[last_message_id][b'INTERNALDATE']

    # returing last mail time .......................
    return received_time


# function for getting the subject and body of the last received mail ...........
def geLastMailtSubjectAndBody():
    # connect to your email server .........................
    mail = imaplib.IMAP4_SSL(imap_server)
    mail.login(imap_username, imap_password)
    mail.select('inbox')

    # searching for the latest email ..................
    result, data = mail.search(None, 'ALL')
    latest_email_id = data[0].split()[-1]

    # retrieve the email message .......................
    result, data = mail.fetch(latest_email_id, '(RFC822)')
    raw_email = data[0][1]
    email_message = email.message_from_bytes(raw_email)

    # extracting the subject and body ....................
    subject = email_message['subject']
    body = ''

    if email_message.is_multipart():
        for part in email_message.walk():
            content_type = part.get_content_type()
            if content_type == 'text/plain':
                body += part.get_payload(decode=True).decode('utf-8')
    else:
        body = email_message.get_payload(decode=True).decode('utf-8')

    # returning the dict of subject as key and body as value ..................
    subjectAndBody = {subject: body}
    return subjectAndBody


# Function to get resheduled lecture id and time ...............
def perform_Reshedule(body, ids):
    sum = 0
    for data in ids:
        sum = sum + data

    # getting the id from the string and performing  ..............
    id = body[0:2]
    sum = sum + int(id)
    resheduledid = (12 - sum)

    # Converting the data and time string in datetime format .............
    from datetime import datetime
    dateAndTime = datetime.strptime(body[3:], '%Y-%m-%d %H:%M')

    # sending mail to the resheduled faculty .........................
    dict = {resheduledid: dateAndTime}
    VandD.resheduledDateAndTimeDict = dict
    send_Mail_To_Resheduled_Faculty(dict)


# function to send mail to faculty who is going to attend resheudeld lecture ............
def send_Mail_To_Resheduled_Faculty(dict):
    id = list(dict.keys())[0]
    DateTime = list(dict.values())[0]
    message = "Hello " + str(faculty_name[(id-1)]) + ", \nYou have a lecture reshedule notice.\nLecture Time : " + str(DateTime.hour) + " : " + str(
        DateTime.minute) + " on TE E&TC class. \n So please report on time we will " + "send an remainder mail befor 10 minutes for your conveinence."
    sendMail(faculty_mail[(id-1)], message)


# function to get id and time for the resheduled lecture ........
def get_Reshedule_ID_And_Time():
    return VandD.resheduledDateAndTimeDict

# function to check whether a lecture is rescheduled or not ......................
def get_Is_Resheduled():
    return VandD.is_resheduled

# function for getting ids to reschedule the lectures accoring to current day ........................
def getResheduleIds():
    current_date = datetime.date.today()
    current_day = current_date.strftime("%A")

    if (current_day == "Monday"):
        return mondayresheduleid

    elif (current_day == "Tuesday"):
        return tuesdayresheduleid

    elif (current_day == "Wednesday"):
        return wednesdayresheduleid

    elif (current_day == "Thursday"):
        return thursdayresheduleid

    elif (current_day == "Friday"):
        return fridayresheduleid

# main thread of rescheduing starts from here ...............
def check_And_Perform_reshedule():
    print("Reshedule Thread is started ................")

    # getting rescheding ids and print on terminal .....................
    ids = getResheduleIds()
    print(f"Reshedule ids are {ids}")
    reshedule_Subject = "Reshedule lecture"

    # infinte loop for continous accessment ...........................
    while True:
        # getting current date and time .......................
        now = datetime.datetime.now()
        # getting the last mail time .............
        rec = getLastMailTime()
        # if last mail time == to current time then execute if block ....................
        if ((rec.hour == now.hour) & (rec.minute == now.minute)):
            # grtting the subject and the body of the last mail .............
            subject_And_body = geLastMailtSubjectAndBody()
            subject = list(subject_And_body.keys())[0]
            body = list(subject_And_body.values())[0]
            # if subject is "Reshedule lecture" then perfom reshedule ...........
            if (subject == reshedule_Subject):
                perform_Reshedule(body, ids)
                VandD.is_resheduled = True

        # if last mail time != current time then execute else block ................
        else:
            print("wating for mail")
            VandD.is_resheduled = False

        # go to sleep mode for a minute .......................
        time.sleep(60)
