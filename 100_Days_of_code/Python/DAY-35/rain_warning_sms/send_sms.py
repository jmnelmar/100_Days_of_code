
import os
from twilio.rest import Client

class TwilioSms:
    def __init__(self):
        self.__account_sid = os.environ['TWILIO_ACCOUNT_SID']
        self.__auth_token = os.environ['TWILIO_AUTH_TOKEN']
        self.__number = '+19382539870'
    
    def sendSMS(self, number, message):
        client = Client(self.__account_sid,self.__auth_token)
        request = client.messages.create(
            body = message,
            from_ = self.__number,
            to = number
        )

