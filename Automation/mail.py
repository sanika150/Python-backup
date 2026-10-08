import smtplib
from email.message import EmailMessage

def send_mail(sender,app_password,receiver,subject,body):
    #step 1 :Create email object
    msg = EmailMessage()

    #step 2:set mail header
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    #step 3:add mail body
    msg.set_content(body)
    #step 4:create smtp ssl connection manually
    smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)
    #step 5:login using gmail and app password
    smtp.login(sender,app_password)
    #step 6:send email
    smtp.send_message(msg)
    #step 7 :close connection mannually
    smtp.quit()

def main():
    sender_email="chikushetye21@gmail.com"

    app_password="wflf gwot ugzj rlot"

    receiver_email = "sanikadhamnaskar15@gmail.com"

    subject = "Test Mail from Python Script"

    body ="""Jay Ganesh",
This is a test email sent using Marvellous Python.

Regards,
Sanika Dhamnaskar"""

    send_mail(sender_email,app_password,receiver_email,subject,body)

    print("Marvellous mail sent Successfully")

if __name__ == "__main__":
    main()