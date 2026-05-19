import smtplib
import ssl
import os
from dotenv import load_dotenv

load_dotenv()
def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "zviadd97@gmail.com"
    password = os.getenv("EMAIL_PASSWORD")

    receiver = "zviadd97@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
        

if __name__ == "__main__":
    send_email("Hello, how are you?")
