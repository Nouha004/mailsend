import smtplib
from email.message import EmailMessage
import os

EMAIL = os.environ["GMAIL_USER"]
PASSWORD = os.environ["GMAIL_APP_PASSWORD"]
TO = os.environ["TO_EMAIL"]

msg = EmailMessage()
msg["Subject"] = "☀️ Morning Reminder"
msg["From"] = EMAIL
msg["To"] = TO
msg.set_content(
    "Good morning!\n\nThis is your daily reminder sent by GitHub Actions.\n\nHave a great day 🚀"
)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(EMAIL, PASSWORD)
    server.send_message(msg)
