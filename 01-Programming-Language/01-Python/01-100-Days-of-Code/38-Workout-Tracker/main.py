import requests
from datetime import datetime

activity_list=[]
## NUTRITIONIX
APP_ID=""
APP_KEY=""

GENDER="male"
WEIGHT=60
HEIGHT = 168
AGE = 25

endpoint_nutritionix = "https://trackapi.nutritionix.com/v2/natural/exercise"

## SHEETY
USERNAME=""
PROJECTNAME="myWorkouts"
SHEETNAME="workouts"
SHEETY_AUTH = ""
endpoint_sheety =f"https://api.sheety.co/{USERNAME}/{PROJECTNAME}/{SHEETNAME}"

## PARAMS
headers = {
    "x-app-id":APP_ID,
    "x-app-key":APP_KEY,
    "Content-Type":"application/json",
}
body = {
    "query":"Walk 10km and run 5km",
    "gender": GENDER,
    "weight_kg":WEIGHT,
    "height_cm":HEIGHT,
    "age":AGE,
}

headers_sheety = {
    "Authorization": SHEETY_AUTH
}

response = requests.post(url=endpoint_nutritionix,json=body,headers=headers)
data = response.json()["exercises"]

# Put activities into list
for entry in data:
    activity = [entry["user_input"],entry["duration_min"],entry["nf_calories"]]
    activity_list.append(activity)

## Post to Excel
date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S")

for activity in activity_list:
    body = {
        'workout': 
            {
                'date': date,
                'time': time, 
                'exercise': activity[0], 
                'duration': activity[1], 
                'calories': activity[2], 
            }
        }
    response_update = requests.post(url=endpoint_sheety,json=body,headers=headers_sheety)
    print(response_update.text)
