#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime

datamanager = DataManager()
datamanager.update_IATA()
datamanager.get_city()

flightsearch = FlightSearch()
flights = []
response = flightsearch.search(fly_to="PAR")

for city in datamanager.IATA:
    response = flightsearch.search(fly_to=city)

    flights.append([
        response["data"][0]["flyFrom"],
        response["data"][0]["cityFrom"],
        datetime.utcfromtimestamp(response["data"][0]["route"][0]['dTimeUTC']).date(),
        response["data"][0]["flyTo"],
        response["data"][0]["cityTo"],
        datetime.utcfromtimestamp(response["data"][0]["route"][1]['dTimeUTC']).date(),
        response["data"][0]["conversion"]["GBP"]
        ])
    print(f"{city} flights added.")


print(flights)

notificationmanager = NotificationManager()
notificationmanager.notify(flights=flights,price_dict=datamanager.price_dict)