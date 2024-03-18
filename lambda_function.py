import smtplib, ssl, os
from cell_providers import PROVIDERS
from receiver_list import RECEIVERS
from message_type import MESSAGES

def lambda_handler(event, context):
    def send_sms_via_email(
    number: str,
    message: str,
    provider: str,
    sender_credentials: tuple,
    subject: str = "Sent with python from AWS",
    smtp_server: str = "smtp.gmail.com",
    smtp_port: int = 465,
    ):
        
        sender_email, email_password = sender_credentials
        receiver_email = f'{number}@{PROVIDERS.get(provider).get("sms")}'
        email_message = f"Subject:{subject}\nTo:{receiver_email}\n{message}"

        with smtplib.SMTP_SSL(
            smtp_server, smtp_port, context=ssl.create_default_context()
        ) as email:
            email.login(sender_email, email_password)
            email.sendmail(sender_email, receiver_email, email_message)

    sender_credentials = (os.getenv('SMTP_EMAIL'), os.getenv('SMTP_PASSWORD'))
    for name, details in RECEIVERS.items():
        number = details['phone_number']
        message = f'Greetings {name}! \n'
        for message_type in details['message_type']:
            message += MESSAGES[message_type] + '\n'
        provider = details['provider']
        send_sms_via_email(number, message, provider, sender_credentials)
