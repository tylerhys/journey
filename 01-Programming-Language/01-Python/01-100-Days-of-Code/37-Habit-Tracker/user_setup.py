import requests

PIXELA_ENDPOINT="https://pixe.la/v1/users"

## User Setup (one time)
user_params={
    "token":"",
    "username":"",
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

response = requests.post(url=PIXELA_ENDPOINT,json=user_params)
print(response.text)