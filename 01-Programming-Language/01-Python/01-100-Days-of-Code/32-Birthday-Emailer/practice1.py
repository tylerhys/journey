import smtplib

my_email = "tylerhystesting@gmail.com"
password = "giay calq sudm hayl"


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="tylerhys98@gmail.com",
        msg="Subject:Hello\n\nThis is the content"
        )