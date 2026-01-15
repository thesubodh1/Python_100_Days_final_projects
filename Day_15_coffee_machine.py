initial_resources = {
    "Water" :300,
    "Milk":200,
    "Coffee":100,
    "Money" :0
}

Espresso = {
    "Water":50,
    "Coffee":18,
    "Milk":0,
    "Price":1.50,
}

Latte = {
    "Water":200,
    "Coffee":24,
    "Milk":150,
    "Price":2.50
}

Cappuccino = {
    "Water" : 250,
    "Coffee" : 24,
    "Milk":100,
    "Price":3.00
}

def check_resources(drink_name):
    if initial_resources["Water"] >= drink_name["Water"]:
        if initial_resources["Coffee"] >= drink_name["Coffee"]:
            if initial_resources["Milk"] >= drink_name["Milk"]:
                return True
            else:
                print("Sorry!! We ran out of coffee")
                return False
        else:
            print("Sorry!! we ran out of Coffee")
            return False
    else:
        print("Sorry!! We ran out of water.")
        return False

def process_coin(drink_name):
    print("Please Insert Coins")
    quarters = float(input("How many quarters:- "))
    dimes = float(input("How many dimes:- "))
    nickles = float(input("How many nickles:- "))
    penny = float(input("How many penny:- "))

    total_money  = round((quarters*0.25) + (dimes * 0.10)  + (nickles * 0.05) + (penny * 0.01),2)
    print(total_money)
    required_amount = drink_name["Price"]
    if total_money >= required_amount:
        print(f"Here is your change: {round(total_money - required_amount,2)}")
        process_resources(initial_resources,drink_name)
        return True
    elif total_money == required_amount:
        return  True
    else:
        print("Sorry!! The coins are insufficient")
        return  False

def process_resources(total_resources,drink_name):
    rem_water = total_resources["Water"] - drink_name["Water"]
    rem_milk = total_resources["Milk"] - drink_name["Milk"]
    rem_coffee = total_resources["Coffee"] - drink_name["Coffee"]
    rem_money = total_resources["Money"] + drink_name["Price"]
    global  initial_resources
    initial_resources = {
        "Water" : rem_water,
        "Milk" : rem_milk,
        "Coffee":rem_coffee,
        "Money":rem_money
    }

def report():
    print(f"Water: {initial_resources["Water"]}l\nMilk: {initial_resources["Milk"]}l\nCoffee: {initial_resources["Coffee"]}gm\nMoney :${initial_resources["Money"]}")

is_on = True
while is_on:
    drink = ""
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").capitalize()
    if user_choice == "Latte":
        drink = Latte
    elif user_choice == "Espresso":
        drink = Espresso
    elif user_choice == "Report":
        report()
        continue
    elif user_choice == "Cappuccino":
        drink =  Cappuccino

    elif user_choice == "Off":
        is_on = False
        continue

    else:
        print("Please select among the available Drinks")
        continue

    if check_resources(drink):
        if process_coin(drink):
            print(f"Enjoy is your {user_choice}")


