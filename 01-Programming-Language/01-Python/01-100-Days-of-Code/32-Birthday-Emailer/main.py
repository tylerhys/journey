import smtplib
import pandas as pd
from random import randint
import datetime as dt

my_email = "tylerhystesting@gmail.com"
password = "giay calq sudm hayl"
INBDAY = "01-Programming-Language\\01-Python\\01-100-Days-of-Code\\32-Birthday-Emailer\\birthdays.csv"
# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()

bdaylist = pd.read_csv(INBDAY).values.tolist()

for entry in bdaylist:
    if today.day == entry[4] and today.month == entry[3]:
        with open(f"01-Programming-Language\\01-Python\\01-100-Days-of-Code\\32-Birthday-Emailer\\letter_templates\\letter_{randint(1,3)}.txt") as file:
            body = file.read()
            body = body.replace("[NAME]",entry[0])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=entry[1],
                msg=f"Subject:Happy Birthday\n\n{body}"
                )




