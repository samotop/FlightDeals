from twilio.rest import Client
import smtplib
import os

TWILLIO_AUTH_TOKEN = os.environ.get("TWILLIO_AUTH_TOKEN")
TWILLIO_API_KEY = os.environ.get("TWILLIO_API_KEY")
ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
MY_NUMBER = os.environ.get("MY_NUMBER")
MY_EMAIL = os.environ.get("MY_EMAIL")
EMAIL_PASS = os.environ.get("EMAIL_PASS")


class NotificationManager:

    def send_sms(self, text_message):
        client = Client(ACCOUNT_SID, TWILLIO_AUTH_TOKEN)

        message = client.messages \
            .create(
            body=text_message,
            from_='+12564149445',
            to= MY_NUMBER
        )

    def send_email(self, text_message, user_email):
        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.ehlo('Gmail')
        connection.starttls()
        connection.login(user=MY_EMAIL, password=EMAIL_PASS)
        try:
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=user_email,
                                msg=f"Subject:Cheap Flight Alert!\n\n{text_message}".encode("utf-8"))
            connection.close()

        except smtplib.SMTPRecipientsRefused:
            print("Wrong email.")