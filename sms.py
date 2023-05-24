import tkinter as tk
from tkinter import messagebox, Text

from email.message import EmailMessage
import ssl
import smtplib

import numpy as np
import pandas as pd


class App:
    text: Text

    # Generating the gui
    def __init__(self, master):
        self.master = master
        master.title("Students Messaging System")
        self.master.geometry("700x600")
        self.master.pack_propagate(0)

        self.headLabel = tk.Label(master,
                                  text="Students Messaging System",
                                  font=("Times New Roman", 40),
                                  height=2,
                                  width=40
                                  )
        self.headLabel.pack()

        self.label_Subject = tk.Label(
            master, text="Enter a message : ", font=("Times New Roman", 20), pady=25)
        self.label_Subject.pack()

        self.text_Subject = tk.Text(root, width=50, height=2, padx=10, pady=10)
        self.text_Subject.pack()

        self.label = tk.Label(master, text="Enter a message : ", font=(
            "Times New Roman", 20), pady=25)
        self.label.pack()

        self.text = tk.Text(root, width=50, height=5, padx=25, pady=25)
        self.text.pack()

        self.submit_button = tk.Button(
            master, text="Submit", command=self.display_message, padx=10, pady=10)
        self.submit_button.pack()

    def display_message(self):
        df = pd.read_csv('studdata.csv')
        # Access the data in the desired column using the column name
        email_of_student = df['Email']

        # Convert the data to a NumPy array for further processing
        mail_Address = np.array(email_of_student)

        subject = self.text_Subject.get("1.0", tk.END)
        message = self.text.get("1.0", tk.END)

        try:
            self.sendMail(mail_Address, subject, message)
            messagebox.showinfo(message="Mails are sent to all the students.")
        except:
            messagebox.showinfo(
                message="Please check the Internet connection.")

    @staticmethod
    def sendMail(email_receiver, subject, body):
        email_sender = "bharambepratik2002@gmail.com"
        email_password = "yhexjdsegqiforwq"

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


root = tk.Tk()
app = App(root)
root.mainloop()
