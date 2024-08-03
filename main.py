import requests, time
from datetime import datetime, timedelta
from twilio.rest import Client
import os
from dotenv import load_dotenv


load_dotenv()


now = datetime.now()
now_plus_10 = now + timedelta(minutes = 10)

data = requests.get("https://demo.transiter.dev/systems/us-ny-subway/stops/D28").json()

firstStopTime = []
for train_details in data["stopTimes"]:
    if train_details["trip"]["destination"]["name"] == "96 St" or train_details["trip"]["destination"]["name"] == "Bedford Park Blvd":
        firstStopTime.append(train_details)

notification_message= []

for i in firstStopTime:
    arrival_time = int(i["arrival"]["time"])
    arrival_time_in_minutes = int((arrival_time - time.time()) / 60)
    now = datetime.now()
    expected_time = now + timedelta(minutes=arrival_time_in_minutes)
    ex_time = expected_time.time()
    timevalue_12hour = ex_time.strftime("%I:%M %p")
    # print(f"The {i["trip"]["route"]["id"]} arrives at {timevalue_12hour}, this train goes to {i["destination"]["name"]}")
    text = f"The {i["trip"]["route"]["id"]} arrives at {timevalue_12hour}, this train goes to {i["destination"]["name"]}"
    notification_message.append(text)

if len(notification_message) == 0:
    print("There are no trains at this time")
else:
    for i in range(int(len(firstStopTime)/2)):
        client = Client(os.getenv("ACCOUNT_SID"), os.getenv("AUTH_TOKEN"))
        message = client.messages.create(
            from_=f'whatsapp:+{os.getenv("TWILIO_NUMBER")}',
            body=notification_message[i],
            to=F'whatsapp:+{os.getenv("MY_PHONE_NUMBER")}'
        )
        print(message.status)
        print(message.sid)
