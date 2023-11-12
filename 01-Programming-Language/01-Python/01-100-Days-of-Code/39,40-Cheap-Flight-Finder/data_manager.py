import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.API_KIWI = ""
        self.URL_KIWI = "https://api.tequila.kiwi.com/"
        self.URL_SHEETY = "https://api.sheety.co/224160ccf16579d4590f7617cd3d899d/flightDeals/prices/"
        self.TOKEN_SHEETY = {
            "Authorization": "Bearer"
        }
        self.city_list=[]
        self.IATA=[]
        self.price_dict={}

    def get_city(self):
        response = requests.get(url=f"{self.URL_SHEETY}",headers=self.TOKEN_SHEETY).json()['prices']
        self.price_list = [data["city"] for data in response]

    def get_price(self):
        response = requests.get(url=f"{self.URL_SHEETY}",headers=self.TOKEN_SHEETY).json()['prices']
        
        for data in response:
            self.price_dict[data["IATA Code"]] = data["Lowest Price"]

    def get_IATA(self,country):
        parameters = {
            "term":country,
            "location_types":"city"
        }

        header = {
            "apikey":self.API_KIWI
        }
        response_kiwi = requests.get(url=f"{self.URL_KIWI}locations/query",params=parameters,headers=header)
        return response_kiwi.json()["locations"][0]["code"]

    def update_IATA(self):
        index = 2
        self.get_city()
        for city in self.city_list:
            code = self.get_IATA(city)
            self.IATA.append(code)
            body = {
                "price":{
                    "iataCode":code
                }
            }

            response = requests.put(url=f"{self.URL_SHEETY}/{index}",headers=self.TOKEN_SHEETY,json=body)
            response.raise_for_status()
            index += 1 