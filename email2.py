import smtplib
from email.message import EmailMessage

def email_message(subject , body , to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to


    user = "lucifer.ai.288@gmail.com"
    msg['from'] = user
    password = "mfbjcjevynjezpaz"

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)
    print("mail sent")
    server.quit()

subject=input("enter subject:")
to=input("enter the reciever\'s email address:")
msg=input("enter your message:")
email_message(subject,msg,to)

