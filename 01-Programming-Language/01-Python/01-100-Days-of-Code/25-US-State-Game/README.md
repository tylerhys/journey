## Day 25
csv
```
# import csv (read csv into obj)
csv.reader(file)
```
pandas
```
import pandas
data = pandas.read_csv(file)

# read column
data["column"]
data.column

# get row
print(data[data.column ==  "condition"])

# get element in row
data2 = data[data.column == "condition"]
data2.column2

# create df
pandas.DataFrame(data)

# df to csv
data.to_csv("data.csv")
```
