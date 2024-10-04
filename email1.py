import smtplib
from email.message import EmailMessage

to = input ("Enter the mail id:")
subject= input('Enter the subject:')
body=input("Enter the body:")
def email_message(subject , body , to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    msg['body'] = body


    user = "your-email"
    msg['from'] = user
    password = "mail:app_password"

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)
    print("mail sent")
    server.quit()
email_message(subject , body , to)
