import datetime as dt
from random import choices
import smtplib

my_email = "tylerhystesting@gmail.com"
password = "giay calq sudm hayl"
INFILE = "01-Programming-Language\\01-Python\\01-100-Days-of-Code\\32-Birthday-Emailer\\quotes.txt"
quotelist = []

with open(INFILE) as file:
    quotelist = [quote.strip() for quote in file.readlines()]

if dt.datetime.now().weekday() == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="tylerhys98@gmail.com",
            msg=f"Subject:Quote of The Day\n\n{choices(quotelist)[0]}"
            )
