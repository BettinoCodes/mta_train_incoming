import requests, time
from datetime import datetime, timedelta

class MessageStorage:
    def __init__(self):
        self.data = requests.get("https://demo.transiter.dev/systems/us-ny-subway/stops/D28").json()
        self.arrival_times = []
        self.notification_messages= []


    def add_to_arrival(self):
        for train_details in self.data["stopTimes"]:
            if train_details["trip"]["destination"]["name"] == "96 St" or train_details["trip"]["destination"]["name"] == "Bedford Park Blvd":
                self.arrival_times.append(train_details)

    def add_to_notfication_messages(self):
        for i in self.arrival_times:
            arrival_time = int(i["arrival"]["time"])
            arrival_time_in_minutes = int((arrival_time - time.time()) / 60)
            now = datetime.now()
            expected_time = now + timedelta(minutes=arrival_time_in_minutes) - timedelta(hours=4)
            ex_time = expected_time.time()
            timevalue_12hour = ex_time.strftime("%I:%M %p")
            # print(f"The {i["trip"]["route"]["id"]} arrives at {timevalue_12hour}, this train goes to {i["destination"]["name"]}")
            text = f"The {i['trip']['route']['id']} arrives at {timevalue_12hour}, this train goes to {i['destination']['name']}"
            self.notification_messages.append(text)
