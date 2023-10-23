import art
import os

end = False

def add(a,b):
    return a + b

def min(a,b):
    return a - b

def mlt(a,b):
    return a * b

def div(a,b):
    return a / b

while not end:
    print(art.logo)
    
    end2 = False
    x = float(input("What's the first number?: "))
    print("+\n-\n*\n/\n")
    while not end2:
        op = input("Pick an operation: ")
        y = float(input("What's the next number?: "))
        
        calc = {
            "+": add(x,y),
            "-": min(x,y),
            "*": mlt(x,y),
            "/": div(x,y),
        }
        result = calc[op]
        print(f"{x} {op} {y} = {result}")
        conti = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        if conti == "n":
            end2 = True
            os.system('cls')
        else:
            x = result
    