import os
import smtplib
from email.message import EmailMessage

user_gmail = os.getenv('USER_GMAIL')
password_gmail = os.getenv('PASSWORD_GMAIL')
msg=EmailMessage()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

def send_notifying_mail(mail_user: str = "", mail_password: str = "") -> None:
    cuerpo="Hola desde colab"
    msg.set_content(cuerpo)
    server.login(user_gmail,password_gmail)
    server.send_message(msg)
    server.quit()

send_notifying_mail(user_gmail, password_gmail)

if __name__ == "__main__":
      send_notifying_mail(user_gmail, password_gmail)
