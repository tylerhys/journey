import requests
from datetime import datetime

PIXELA_ENDPOINT="https://pixe.la/v1/users"
TOKEN=""
USERNAME=""
ID="graph1"
NAME="Cycling Graph"
UNIT="Km"
TYPE="float"
COLOR="ichou"


graph_endpoint=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_params={
    "id":ID,
    "name":NAME,
    "unit":UNIT,
    "type":TYPE,
    "color":COLOR
}
header = {
    "X-USER-TOKEN":TOKEN
}

## Create Graph (ONE TIME)
# response = requests.post(url=graph_endpoint,json=graph_params,headers=header)
# print(response.text)

## Create Pixel
today = datetime.now().strftime("%Y%m%d")

pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{ID}/"
pixel_data = {
    "date":f"{today}",
    "quantity":"10",
}
# response = requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=header)
# print(response.text)

## Update Pixel
pixel_update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{ID}/{today}"
update_data = {
    "quantity":"20",
}
# response = requests.put(url=pixel_update_endpoint,json=update_data,headers=header)
# print(response.text)

## Delete Pixel
pixel_delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{ID}/{today}"

response = requests.delete(url=pixel_update_endpoint,headers=header)
print(response.text)