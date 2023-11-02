## Day 27
Tkinter
```
Pack() documentation:  [Link](https://docs.python.org/3/library/tkinter.html#the-packer)
```
unlimited arg func
```
def func(*agrs):
    for n in args:
        print (args)
```
key word args
```
#kwargs is an object
def func(**kwargs):
    for key,value in kwargs.items():
        print(key)
        print(value)

func(key=value,key2=value...)
```