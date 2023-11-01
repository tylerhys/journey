## Day 26
list comprehension
```
new_list = [new_item for item in list if condition]

numbers = [1,2,3]
new_numbers = [n + 1 for n in numbers]
```
dict comprehension
```
new_dict={new_key:new_value for item in list}
new_dict={new_key:new_value for (key,value) in dict.items() if condition}
```
Loop Through Pandas
```
for (index,row) in df.iterrows():
    print(index)
    print(row.element)
```