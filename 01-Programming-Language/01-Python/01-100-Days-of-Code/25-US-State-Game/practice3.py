import pandas

INPATH = "01-Programming-Language\\01-Python\\01-100-Days-of-Code\\25-US-State-Game\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
OUTPATH = "01-Programming-Language\\01-Python\\01-100-Days-of-Code\\25-US-State-Game\\Fur_Count.csv"
data = pandas.read_csv(INPATH)

data_fur = pandas.DataFrame(data["Primary Fur Color"].value_counts())
data_fur.to_csv(OUTPATH)
