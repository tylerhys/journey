import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.API_KIWI = ""
        self.URL_KIWI = "https://api.tequila.kiwi.com/"
        self.fly_from = "LON"

    def search(self,fly_to):
        date_from = (datetime.now() + relativedelta(days=+1)).strftime("%d/%m/%Y")
        date_to = (datetime.now() + relativedelta(days=+1,months=+6)).strftime("%d/%m/%Y")
        parameters = {
            "fly_from":self.fly_from,
            "fly_to":fly_to,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from":3,
            "nights_in_dst_to":7,
            "flight_type":"round",
            "one_for_city":1,
            "max_stopovers":0,
            "adults":1,
            "selected_cabins":"M",
            "curr":"GBP"
        }

        header = {
            "apikey":self.API_KIWI
        }

        response_kiwi = requests.get(url=f"{self.URL_KIWI}search",params=parameters,headers=header)
        return response_kiwi.json()