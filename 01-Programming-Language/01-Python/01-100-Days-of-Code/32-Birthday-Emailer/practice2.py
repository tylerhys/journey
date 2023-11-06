import datetime as dt

now = dt.datetime.now()
print(now)

year = now.year
print(year)

day = now.weekday()
print(day)

date_of_birth = dt.datetime(year=1998,month=2,day=3)
print(date_of_birth)