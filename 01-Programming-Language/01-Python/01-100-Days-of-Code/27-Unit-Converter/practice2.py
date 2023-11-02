def add(*args):
    total = 0
    for n in args:
        total += n

    return total

print(add(1,2,3,4,5))

def calculate(**kwargs):
    print(kwargs)

calculate(add=3,add2=4)

class Car:
    def __init__(self,**kw) -> None:
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")

my_car = Car(make="Nissan")
