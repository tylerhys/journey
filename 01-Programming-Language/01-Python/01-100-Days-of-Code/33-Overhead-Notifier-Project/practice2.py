import requests
from datetime import datetime

LAT = 3.140853
LNG = 101.693207

parameters = {
    "lat": LAT,
    "lng": LNG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()
print(data)
sunrise = (int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 8) % 24
sunset = (int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 8 ) % 24

time_now = datetime.now()

print(sunrise,sunset,time_now.hour)

