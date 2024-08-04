import requests, time
from datetime import datetime, timedelta
from twilio.rest import Client
import os
from dotenv import load_dotenv
from notification import NotificationManager
from message_storage import MessageStorage


load_dotenv()

notification_manager = NotificationManager()
messages_stored = MessageStorage()


messages_stored.add_to_arrival()
messages_stored.add_to_notfication_messages()

if len(messages_stored.notification_messages) == 0:
    print("There are no trains at this time")
else:
    notification_manager.send_messages_from_list(messages_stored.notification_messages)

