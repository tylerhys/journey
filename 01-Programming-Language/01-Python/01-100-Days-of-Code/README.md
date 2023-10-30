## **Day 19,20**
Inheritance
```
## Use super(). to call anything from parent class
class Fish(Animal):
    def __init__(self):
        super().__init__()
```
Slice
```
#works for lists and tuples
List=[a,b,c,d,e,f]
List[2:5] => [c,d,e]
List[2:] => [c,d,e,f]
List[2:5:2] => [c,e]
List[::-1] => [f,e,d,c,b,a]
```