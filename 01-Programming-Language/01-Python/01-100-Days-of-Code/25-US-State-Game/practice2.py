import pandas

INPATH = "01-Programming-Language\\01-Python\\01-100-Days-of-Code\\25-US-State-Game\\weather_data.csv"

data = pandas.read_csv(INPATH)
print(type(data))
print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

print(data["temp"].mean())
print(data["temp"].max())

print(data[data.day ==  "Monday"])
print(data[data.temp == data["temp"].max()])

monday = data[data.day == "Monday"]
print((monday.temp.iloc[0] * 9 / 5)+32)