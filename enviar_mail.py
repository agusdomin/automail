import os
import smtplib
from email.message import EmailMessage

user_gmail = os.getenv('USER_GMAIL')
password_gmail = os.getenv('PASSWORD_GMAIL')

def send_notifying_mail(mail_user: str = "", mail_password: str = "") -> None:
    # aqui va tu codigo
    ...

send_notifying_mail(user_gmail, password_gmail)

if __name__ == "__main__":
      send_notifying_mail(user_gmail, password_gmail)
