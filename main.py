#Work is still in progress
import requests
from pprint import pprint
import requests, time
from datetime import datetime, timedelta
#Need to import twillio

now = datetime.now()
now_plus_10 = now + timedelta(minutes = 10)

data = requests.get("https://demo.transiter.dev/systems/us-ny-subway/stops/D28").json()

firstStopTime = []
for train_details in data["stopTimes"]:
    if train_details["trip"]["destination"]["name"] == "96 St":
        firstStopTime.append(train_details)

for i in firstStopTime:
    arrival_time = int(i["arrival"]["time"])
    arrival_time_in_minutes = int((arrival_time - time.time()) / 60)
    now = datetime.now()
    expected_time = now + timedelta(minutes=arrival_time_in_minutes)
    ex_time = expected_time.time()
    timevalue_12hour = ex_time.strftime("%I:%M %p")
    print(f"The {i["trip"]["route"]["id"]} arrives at {timevalue_12hour}, this train goes to {i["destination"]["name"]}")
