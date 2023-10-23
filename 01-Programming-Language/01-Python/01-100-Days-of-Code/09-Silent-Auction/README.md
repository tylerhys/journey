## **Day 9**
Dictionaries
```
dict = {
    "item1":"abc",
    "item2":"def",
}

# Add entries
dict["item3"] = "ghi"

# Edit value
dict["item1"] = "aaa"

# Loop thru dict
for key in dict:
    print (key)
    print (dict[key])

# Nesting 
dict = {
    "key1":["x","y","z"],
    "key2":["a","b","c"]
}

# dict in dict
dict = {
    {
        "key1": "abc",
        "key2": "efg",
    },
    {
        "key3": "abc",
        "key4": "efg",
    }
}
```
