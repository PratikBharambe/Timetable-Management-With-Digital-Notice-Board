import datetime
import time
import threading

from email.message import EmailMessage
import ssl
import smtplib

import reSheduleLecture as re

import numpy as np
import pandas as pd


df = pd.read_csv('tefaculty.csv')

# Access the data in the desired column using the column name
Faculty_ID = df["id"]
Faculty_name = df["name of faculty"]
Faculty_Mail = df["mail"]
Faculty_subject = df["subject"]

# Convert the data to a NumPy array for further processing
faculty_id = np.array(Faculty_ID)
faculty_name = np.array(Faculty_name)
faculty_mail = np.array(Faculty_Mail)
faculty_subject = np.array(Faculty_subject)

mondaylecturesid = [4, 3, 5, 3, 4]
tuesdaydaylecturesid = [4, 3, 5, 7, 4]
wednesdaylecturesid = [1, 2, 3, 6, 7, 3, 2]
thursdaylecturesid = [1, 2, 7, 4, 6]
fridaydaylecturesid = [4, 1, 4, 6, 5]


def sendMail(email_receiver, body):

    email_sender = "bharambepratik2002@gmail.com"
    email_password = "yhexjdsegqiforwq"
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


def generate_Message_And_send_Mail_for_faculty(ids):
    now = datetime.datetime.now()
    minute = now.minute + 10
    for data in ids:
        if (now.hour == 11):
            message = "Hello " + str(faculty_name[(data-1)]) + ", \nYou have pratical scheduled at time " + str(now.hour) + " : " + str(
                minute) + " on TE E&Tc Class for " + str(faculty_subject[(data-1)]) + " subject.\nSo it's a humble request to report on time on the respetive lab."
            sendMail(faculty_mail[(data-1)], message)
        else:
            message = "Hello " + str(faculty_name[(data-1)]) + ", \nYou have Lecture scheduled at time " + str(now.hour) + " : " + str(
                minute) + " on TE E&Tc Class for " + str(faculty_subject[(data-1)]) + " subject.\nSo it's a humble request to report on time on the respetive classroom."
            sendMail(faculty_mail[(data-1)], message)


# function to follow monday schedule
def mondaySchedule():
    try:
        resheduleThread = threading.Thread(
            target=re.check_And_Perform_reshedule)
        resheduleThread.start()
    except:
        print(
            "Error in starting reshedule thread ..................\nPlease contact the KP")
    while True:
        now = datetime.datetime.now()

        if now.hour == 9 and now.minute == 5:
            if (re.get_Is_Resheduled()):
                idAndTime = re.get_Reshedule_ID_And_Time()
                id = list(idAndTime.keys())[0]
                generate_Message_And_send_Mail_for_faculty([id])
            else:
                generate_Message_And_send_Mail_for_faculty(
                    [mondaylecturesid[0]])
            time.sleep(60)

        elif now.hour == 10 and now.minute == 5:
            if (re.get_Is_Resheduled()):
                idAndTime = re.get_Reshedule_ID_And_Time()
                id = list(idAndTime.keys())[0]
                generate_Message_And_send_Mail_for_faculty([id])
            else:
                generate_Message_And_send_Mail_for_faculty(
                    [mondaylecturesid[1]])
            time.sleep(60)

        elif now.hour == 11 and now.minute == 20:
            if (re.get_Is_Resheduled()):
                idAndTime = re.get_Reshedule_ID_And_Time()
                id = list(idAndTime.keys())[0]
                generate_Message_And_send_Mail_for_faculty([id])
            else:
                generate_Message_And_send_Mail_for_faculty(
                    [mondaylecturesid[2], mondaylecturesid[3], mondaylecturesid[4]])
            time.sleep(60)

        else:
            print(now)
            time.sleep(60)


# function to follow tuesday schedule
def tuesdaySchedule():
    try:
        resheduleThread = threading.Thread(
            target=re.check_And_Perform_reshedule)
        resheduleThread.start()
    except:
        print("Error in starting thread")
    print("tuesday thread Started")
    while True:
        now = datetime.datetime.now()
        if now.hour == 9 and now.minute == 5:
            if (re.get_Is_Resheduled()):
                idAndTime = re.get_Reshedule_ID_And_Time()
                id = list(idAndTime.keys())[0]
                generate_Message_And_send_Mail_for_faculty([id])
            else:
                generate_Message_And_send_Mail_for_faculty(
                    [tuesdaydaylecturesid[0]])
            time.sleep(60)

        elif now.hour == 10 and now.minute == 5:
            if (re.get_Is_Resheduled()):
                idAndTime = re.get_Reshedule_ID_And_Time()
                id = list(idAndTime.keys())[0]
                generate_Message_And_send_Mail_for_faculty([id])
            else:
                generate_Message_And_send_Mail_for_faculty(
                    [tuesdaydaylecturesid[1]])
            time.sleep(60)

        elif now.hour == 11 and now.minute == 52:
            if (re.get_Is_Resheduled()):
                idAndTime = re.get_Reshedule_ID_And_Time()
                id = list(idAndTime.keys())[0]
                generate_Message_And_send_Mail_for_faculty([id])
            else:
                generate_Message_And_send_Mail_for_faculty(
                    [tuesdaydaylecturesid[2], tuesdaydaylecturesid[3], tuesdaydaylecturesid[4]])
            time.sleep(60)

        else:
            print(now)
            time.sleep(60)


# function to follow wednesday schedule
def wednesdaySchedule():
    resheduleThread = threading.Thread(target=re.check_And_Perform_reshedule)
    resheduleThread.start()
    while True:
        now = datetime.datetime.now()
        if now.hour == 9 and now.minute == 5:
            if (re.get_Is_Resheduled()):
                idAndTime = re.get_Reshedule_ID_And_Time()
                id = list(idAndTime.keys())[0]
                generate_Message_And_send_Mail_for_faculty([id])
            else:
                generate_Message_And_send_Mail_for_faculty(
                    [wednesdaylecturesid[0]])
            time.sleep(60)

        elif now.hour == 10 and now.minute == 5:
            if (re.get_Is_Resheduled()):
                idAndTime = re.get_Reshedule_ID_And_Time()
                id = list(idAndTime.keys())[0]
                generate_Message_And_send_Mail_for_faculty([id])
            else:
                generate_Message_And_send_Mail_for_faculty(
                    [wednesdaylecturesid[1]])
            time.sleep(60)

        elif now.hour == 11 and now.minute == 20:
            if (re.get_Is_Resheduled()):
                idAndTime = re.get_Reshedule_ID_And_Time()
                id = list(idAndTime.keys())[0]
                generate_Message_And_send_Mail_for_faculty([id])
            else:
                generate_Message_And_send_Mail_for_faculty(
                    [wednesdaylecturesid[2], wednesdaylecturesid[3], wednesdaylecturesid[4]])
            time.sleep(60)

        elif now.hour == 14 and now.minute == 5:
            if (re.get_Is_Resheduled()):
                idAndTime = re.get_Reshedule_ID_And_Time()
                id = list(idAndTime.keys())[0]
                generate_Message_And_send_Mail_for_faculty([id])
            else:
                generate_Message_And_send_Mail_for_faculty(
                    [wednesdaylecturesid[5]])
            time.sleep(60)

        elif now.hour == 15 and now.minute == 5:
            if (re.get_Is_Resheduled()):
                idAndTime = re.get_Reshedule_ID_And_Time()
                id = list(idAndTime.keys())[0]
                generate_Message_And_send_Mail_for_faculty([id])
            else:
                generate_Message_And_send_Mail_for_faculty(
                    [wednesdaylecturesid[6]])
            time.sleep(60)

        else:
            print(now)
            time.sleep(60)


# function to follow thursday schedule
def thursdaySchedule():
    resheduleThread = threading.Thread(target=re.check_And_Perform_reshedule)
    resheduleThread.start()
    print("Current Day thread started .......")
    while True:
        now = datetime.datetime.now()
        print("Hello")
        if now.hour == 9 and now.minute == 5:
            if (re.get_Is_Resheduled()):
                idAndTime = re.get_Reshedule_ID_And_Time()
                id = list(idAndTime.keys())[0]
                generate_Message_And_send_Mail_for_faculty([id])
            else:
                generate_Message_And_send_Mail_for_faculty(
                    [thursdaylecturesid[0]])
            time.sleep(60)

        elif now.hour == 10 and now.minute == 5:
            if (re.get_Is_Resheduled()):
                idAndTime = re.get_Reshedule_ID_And_Time()
                id = list(idAndTime.keys())[0]
                generate_Message_And_send_Mail_for_faculty([id])
            else:
                generate_Message_And_send_Mail_for_faculty(
                    [thursdaylecturesid[1]])
            time.sleep(60)

        elif now.hour == 11 and now.minute == 20:
            if (re.get_Is_Resheduled()):
                idAndTime = re.get_Reshedule_ID_And_Time()
                id = list(idAndTime.keys())[0]
                generate_Message_And_send_Mail_for_faculty([id])
            else:
                generate_Message_And_send_Mail_for_faculty(
                    [thursdaylecturesid[2], thursdaylecturesid[3], thursdaylecturesid[4]])
            time.sleep(60)

        else:
            print(now)
            time.sleep(60)


# function to follow friday schedule
def fridaySchedule():
    resheduleThread = threading.Thread(
        target=re.check_And_Perform_reshedule)
    resheduleThread.start()
    while True:
        now = datetime.datetime.now()
        if now.hour == 9 and now.minute == 5:
            if (re.get_Is_Resheduled()):
                idAndTime = re.get_Reshedule_ID_And_Time()
                id = list(idAndTime.keys())[0]
                generate_Message_And_send_Mail_for_faculty([id])
            else:
                generate_Message_And_send_Mail_for_faculty(
                    [fridaydaylecturesid[0]])
            time.sleep(60)

        elif now.hour == 10 and now.minute == 5:
            if (re.get_Is_Resheduled()):
                idAndTime = re.get_Reshedule_ID_And_Time()
                id = list(idAndTime.keys())[0]
                generate_Message_And_send_Mail_for_faculty([id])
            else:
                generate_Message_And_send_Mail_for_faculty(
                    [fridaydaylecturesid[1]])
            time.sleep(60)

        elif now.hour == 11 and now.minute == 20:
            if (re.get_Is_Resheduled()):
                idAndTime = re.get_Reshedule_ID_And_Time()
                id = list(idAndTime.keys())[0]
                generate_Message_And_send_Mail_for_faculty([id])
            else:
                generate_Message_And_send_Mail_for_faculty(
                    [fridaydaylecturesid[2], fridaydaylecturesid[3], fridaydaylecturesid[4]])
            time.sleep(60)

        else:
            print(now)
            time.sleep(60)


def activeCurrentDaySchedule():
    current_date = datetime.date.today()
    current_day = current_date.strftime("%A")

    # conditions to call the schedule methods according to current day
    if (current_day == "Monday"):
        print("Current day is : ", current_day)
        mondayThread = threading.Thread(target=mondaySchedule)
        mondayThread.start()
        print(current_day, "Thread is started .................")

    elif (current_day == "Tuesday"):
        print("Current day is : ", current_day)
        tuesdayThread = threading.Thread(target=tuesdaySchedule)
        tuesdayThread.start()
        print(current_day, "Thread is started .................")

    elif (current_day == "Wednesday"):
        print("Current day is : ", current_day)
        wednesdayThread = threading.Thread(target=wednesdaySchedule)
        wednesdayThread.start()
        print(current_day, "Thread is started .................")

    elif (current_day == "Thursday"):
        print("Current day is : ", current_day)
        thursdayThread = threading.Thread(target=thursdaySchedule)
        thursdayThread.start()
        print(current_day, "Thread is started .................")

    elif (current_day == "Friday"):
        print("Current day is : ", current_day)
        fridayThread = threading.Thread(target=fridaySchedule)
        fridayThread.start()
        print(current_day, "Thread is started .................")

    else:
        print("Today is ", current_day,
              "\nToday is Holiday so, Enjoy your day .............")
        return


# Active current day shedule ................
activeCurrentDaySchedule()
print("Current day thread is started.")
