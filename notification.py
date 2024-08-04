from twilio.rest import Client
import os


class NotificationManager:
    """
    this class is made to manage this data when it comes to the notifications, and having all of the necessary 
    attributes related to sending them
    """
    def __init__(self) -> None:
          self.acc_sid = os.environ["ACCOUNT_SID"]
          self.auth_token = os.environ["AUTH_TOKEN"]
          self.my_phone = os.environ["MY_PHONE_NUMBER"]
          self.twilio_number = os.environ["TWILIO_NUMBER"]

    def send_messages_from_list(self, list_of_times):
        """This function is meant to send all of the data in the list individually as a message"""
        for i in range(int(len(list_of_times)/2)):
                client = Client(self.acc_sid, self.auth_token)
                message = client.messages.create(
                    from_=f'whatsapp:+{self.twilio_number}',
                    body=list_of_times[i],
                    to=F'whatsapp:+{self.my_phone}'
                )
                print(message.status)
                print(message.sid)
