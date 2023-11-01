import csv
import pandas

INPATH = "01-Programming-Language\\01-Python\\01-100-Days-of-Code\\25-US-State-Game\\weather_data.csv"
# using csv
with open(INPATH) as file:
    data = csv.reader(file)
    temperature = []
    for row in data:
        if row[1] == "temp":
            pass
        else:
          temperature.append(int(row[1]))
    print(temperature)

# Using pandas
data2 = pandas.read_csv(INPATH)
print(data2)
print("\n")
print(data2["temp"])
