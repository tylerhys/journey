## **Day 24**

```
# open file
file = open("filename.ext")

# read contents
content = file.read()

# close file
file.close()



# without close
# mode: r:read,w:write,a:append
with open("filename.ext",mode="w") as file:
    content = file.read()
    # do something
    file.write("Hello")
```