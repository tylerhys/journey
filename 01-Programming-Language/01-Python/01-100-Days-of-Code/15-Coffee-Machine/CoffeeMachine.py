import data

end = False
data.resources["money"] = 0

def checkResource(choice):
    for ingredient in data.MENU[choice]["ingredients"]:
        if data.MENU[choice]["ingredients"][ingredient] > data.resources[ingredient]:
            return ingredient
    return "None"

def getCoins():
    coins={"quarters":0.25,"dimmes":0.10,"nickles":0.05,"pennies":0.01}
    total = 0
    for coin in coins:
        total += int(input(f"How many {coin}?: ")) * coins[coin]
    return total

while not end:
    choice = input("What would you like? (espresso/latte/cappuccino)\n").lower()

    if choice == "off":
        end = True
    elif choice == "report":
        print(f'Water: {data.resources["water"]}ml')
        print(f'Milk: {data.resources["milk"]}ml')
        print(f'Coffee: {data.resources["coffee"]}g')
        print(f'Money: ${data.resources["money"]}')
    else:
        missing = checkResource(choice)
        if missing != "None" :
            print(f"Sorry there is not enough {missing}")
        else:
            payment = getCoins()
            if payment < data.MENU[choice]["cost"]:
                print(f"Sorry that's not enough money. Money refunded.")
            else:
                data.resources["money"] += data.MENU[choice]["cost"]
                refund = payment - data.MENU[choice]["cost"]
                
                for ingredient in data.MENU[choice]["ingredients"]:
                    data.resources[ingredient] -= data.MENU[choice]["ingredients"][ingredient]
                
                if refund > 0:
                    print(f"Here is ${refund} in change.")
                
                print(f"Here is your {choice}☕️ . Enjoy!!!")
                

