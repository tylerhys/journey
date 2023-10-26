from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

end = False

while not end:
    choice = input(f"What would you like? ({menu.get_items()})\n").lower()
    
    if choice == "off":
        end = True
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        choice = menu.find_drink(choice)
        if  coffee_maker.is_resource_sufficient(choice):
            if money_machine.make_payment(choice.cost):
                coffee_maker.make_coffee(choice)