# Free Serverless Scheduled Reminder SMS Sender

I thought it would be cool to find a way to automate SMS messages to myself at certain times of the day, but I didn't want to spend any money doing so. 
This project is the results of my research and efforts to do so.

## Getting Started

### Local Set up

For context, we will be using the cell provider's email that is set up to let their users phone number receive emails by using {phone_number}@{provider_domain}. 
This is how we will be "sending" the SMS for free. (We also have the ability, if the provider allows it, to send mms, but I did not need this, and thus did not program it)

First, you will need to set an App Password with google for the gmail account that will be used to send the email, this way the script can send the gmail from the gmail account without needing mfa. This can be set at myaccount.google.com/apppasswords, and will need to have the 'Mail' app name entered.

You should then set the environment variables SMTP_EMAIL with the email of the gmail account, and SMTP_PASSWORD of the newly created app password

After this, create a file named message_type.py with an object MESSAGES that has a list of the messages (strings) you want to send, like the below
```
MESSAGES = [
    "Don't forget to Exercise",
    "Catch up with a friend",
    "Tell someone you care about them"
]
```
Create another file named receiver_list.py with an object RECEIVERS that has all receivers of the SMS messages where:
    "phone_number" is a valid 10 digit phone number
    "provider" is matching a valid provider in the PROVIDERS list, and is the cell provider for the phone number listed
    "message_type" holds the index or indexes of the message from the MESSAGES you would like to be sent
```
RECEIVERS = {    
    "John": {"phone_number": "0000000000", "provider": "Verizon", "message_type": [0,1]},
    "Drew": {"phone_number": "0123456789", "provider": "AT&T", "message_type": [1,2]},
    "Alfred": {"phone_number": "9999999999", "provider": "T-Mobile", "message_type": [0]}
}
```
Keep in mind that SMS has a character limit, so if you want to send many messages from the message list, they must not exceed that limit (I am reading 160, but DYOR)

When the environment variables are set, and the above files are made, you can run the email_to_provider.py script to test locally, and if everything has been configured correctly, this should work great.

### AWS Set up

Create a Zip file with the lambda_function.py, cell_providers.py, message_type.py, and receiver_list.py scripts.

Create an AWS Lambda function and import the zip file (You can run the test at this point)

Create an AWS EventBridge Cloudwatch event as a trigger for the Lambda function

I personally wanted the text to come in at 6 PM daily, so I used this schedule expression cron (0 22 ? * * *)

Finally, enjoy your free SMS notifications.

## Usage

By setting up a few files and creating a Lambda function with an EventBridge trigger, you can create free SMS messages sent on a schedule for yourself (and in my case, to your friends, too). This uses a serverless architecture and will stay under AWS's free tier, as long as you aren't sending tons of messages to lots of people, and using up a lot of resources.

## Technologies Used

- Python3
- Gmail SMTP
- AWS Lambda
- AWS EventBridge

## Contact

For any questions or feedback, feel free to contact me at noahdragoon@hotmail.com.

## Acknowledgements

- Special thanks to Alfredo Sequeida and Keith Galli for their great YouTube tutorials that helped me build and deploy this cool project.