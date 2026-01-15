from coffee_maker import  CoffeeMaker
from money_machine import  MoneyMachine
from menu import  MenuItems, Menu

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_is_on = True
while machine_is_on:
    items = menu.get_items()
    user_choice = input(f"What would you like? ({items}): ").lower()
    if user_choice == "report":
        coffee_maker.report()
        money_machine.report()
        continue
    elif user_choice == "off":
        machine_is_on = False
        continue
    else:
        drink = menu.find_drink(user_choice)
        if drink:
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
