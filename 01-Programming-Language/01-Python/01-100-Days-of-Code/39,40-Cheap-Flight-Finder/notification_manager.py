from twilio.rest import Client

class NotificationManager:
    def __init__(self) -> None:
        self.account_sid = ''
        self.auth_token = ''
        self.client = Client(self.account_sid, self.auth_token)

    def notify(self,flights,price_dict):
        for data in flights:
            if data[6] < price_dict[data[0]]:
                flyFrom = data[0]
                cityFrom = data[1]
                dateFrom = data[2]
                flyTo = data[3]
                cityTo = data[4]
                dateTo = data[5]
                price = data[6]

                message = self.client.messages \
                        .create(
                            body=f"Low price alert! Only ${price} to fly from {cityFrom}-{flyFrom} to {cityTo}-{flyTo},from {dateFrom} to {dateTo}.",
                            from_='+12027938520',
                            #  insert number
                            to='+'
                        )

                print(message.status)