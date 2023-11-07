import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 3.139003 # Your latitude
MY_LONG = 101.686852 # Your longitude
MY_EMAIL = "tylerhystesting@gmail.com"
PASSWORD = "giay calq sudm hayl"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def is_overhead():
    if abs(iss_latitude - MY_LAT) < 5 and abs(iss_longitude - MY_LONG) < 5:
        return True
    else:
        return False

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = (int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 8) % 24
    sunset = (int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 8 ) % 24

    time_now = datetime.now()

    if time_now.hour < sunrise and time_now.hour > sunset:
         return True
    else:
         return False

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    if is_overhead() and is_night():
        print("ISS is above and it is night. Processing email request...")
        with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL,password=PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs="tylerhys98@gmail.com",
                    msg=f"Subject:Look Up\n\nThe ISS is above you in the sky!"
                    )
    else:
        print("Conditions not met... Continue monitoring...")



