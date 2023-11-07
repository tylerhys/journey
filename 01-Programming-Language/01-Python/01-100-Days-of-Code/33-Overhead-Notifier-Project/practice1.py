import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

long = data["iss_position"]["longitude"]
lat = data["iss_position"]["latitude"]

pos = (long,lat)
print(pos)