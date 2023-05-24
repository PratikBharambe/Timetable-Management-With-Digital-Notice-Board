

from email.message import EmailMessage
import ssl
import smtplib

email_sender = "bharambepratik2002@gmail.com"
email_password = "yhexjdsegqiforwq"
email_receiver = "guravneha45@gmail.com"


subject = "Sending mail using python"
body = """

Lorem ipsum dolor sit amet consectetur adipisicing elit. Nostrum dignissimos 
aliquam nesciunt quasi, ea excepturi non, saepe corporis praesentium nihil possimus maiores velit doloribus 
molestias! Sequi numquam eaque nihil totam unde earum dolores illo. Ullam, culpa similique debitis ipsa iusto,
 numquam, minus deleniti quod magni dolorem architecto! Modi neque asperiores deserunt atque corporis facere
   corrupti, numquam quae quo, iusto ducimus nesciunt, autem praesentium maiores! Iure tempora, repellendu
   s eveniet pariatur facere, voluptate ea veritatis praesentium dolorem, ipsam qui quos optio ullam voluptat
   ibus tempore aperiam maiores error rerum! Totam, delectus adipisci quibusdam, 
officia dolore dicta ducimus modi asperiores necessitatibus fuga saepe sint?

"""

em = EmailMessage()

em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = subject
em.set_content(body)


context = ssl.create_default_context()


with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    try:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
    except:
        print("NoInternetConnectionError_PleaseCheckInternetConnection")
