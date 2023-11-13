import requests
import html
from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
KEY_ALPHAVANTAGE = ""
API_NEWS = ""
msglist = []

params_stock = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "outputsize":"compact",
    "apikey":KEY_ALPHAVANTAGE
}

params_news = {
    "q":f"({STOCK} AND {COMPANY_NAME})",
    "language":"en",
    "pageSize":3,
    "apiKey":API_NEWS 
}

## Get Stock info
response_stock = requests.get(url="https://www.alphavantage.co/query",params=params_stock)
response_stock.raise_for_status()
datalist = [value for (key,value) in response_stock.json()["Time Series (Daily)"].items()]
data = datalist[0]

delta = round(abs(float(data['1. open']) - float(data['4. close']))/float(data['1. open']),2)

if float(data['1. open']) > float(data['4. close']):
    text_delta = f"🔻{delta*100}%"
else:
    text_delta = f"🔺{delta*100}%"

## Get News
if delta >= 0.05:
    response_news = requests.get(url="https://newsapi.org/v2/everything",params=params_news)
    response_news.raise_for_status()
    # print(response_news.json()["articles"][0]["title"])
    for articles in response_news.json()["articles"]:
        title = html.unescape(articles["title"])
        brief = html.unescape(articles["description"])
        msg = f"{STOCK}: {text_delta}\n\nHeadline: {title}\n\nBrief: {brief}"
        msglist.append(msg)

## Send SMS
def notify(msg):
    message = client.messages \
                .create(
                        body=f"{msg}",
                        from_='+12027938520',
                    #  insert number
                        to='+'
                    )
    print(message.status)

for msg in msglist:
    notify(msg)

