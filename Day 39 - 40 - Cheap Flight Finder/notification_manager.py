import smtplib
from twilio.rest import Client
import os


TWILIO_SID = os.environ.get('TWILIO_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_TOKEN')
TWILIO_VIRTUAL_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER')
TWILIO_VERIFIED_NUMBER = os.environ.get('MY_PHONE_NUMBER')
MY_SMTP_SERVER = os.environ.get('MY_SMTP_SERVER')
MY_EMAIL = os.environ.get('MY_EMAIL')
MY_EMAIL_PASSWORD = os.environ.get('MY_EMAIL_PASSWORD')


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        """Send sms notification for user."""
        msg = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(msg.sid)

    @staticmethod
    def send_mails(user_data, msg):
        """Send e-mail notification for user."""

        with smtplib.SMTP(MY_SMTP_SERVER) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_EMAIL_PASSWORD)

            message = f'Hey {user_data["firstName"]}\n{msg}'

            connection.sendmail(to_addrs=user_data['email'], from_addr=MY_EMAIL, msg=message)
