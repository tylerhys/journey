import requests
from twilio.rest import Client

# get from  https://console.twilio.com/?frameUrl=/console
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

# get from https://home.openweathermap.org/api_keys
API_KEY=""
OWM_ENDPOINT="https://api.openweathermap.org/data/3.0/onecall"

weather_params = {
    "lat":3.140853,
    "lon":101.693207,
    "appid":API_KEY,
    "exclude":"current,minutely,daily"
}

response = requests.get(url=OWM_ENDPOINT,params=weather_params)
response.raise_for_status
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]

    if int(condition_code) < 700:
        will_rain = True
print(will_rain)
if will_rain:
    message = client.messages \
                .create(
                     body="It's going to rain today. Remember to bring an umbrella☂️",
                     from_='+12027938520',
                    #  insert number
                     to='insert number'
                 )

print(message.status)

