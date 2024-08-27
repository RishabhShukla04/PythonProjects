MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.0,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 2.5,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "profit": 0,
}


def check_resources(drink):

    drink = str(drink)

    if "water" in MENU[drink]["ingredients"]:
        dwater = MENU[drink]["ingredients"]["water"]
        if dwater > resources["water"]:
            print("Not enough water")
            return False
    elif "coffee" in MENU[drink]["ingredients"]:
        dcoffee = MENU[drink]["ingredients"]["coffee"]
        if dcoffee > resources["coffee"]:
            print("Not enough coffee")
            return False
    elif "milk" in MENU[drink]["ingredients"]:
        dmilk = MENU[drink]["ingredients"]["milk"]
        if dmilk > resources["milk"]:
            print("Not enough milk")
            return False

    return True

def check_price(drink):
    pounds = 0
    pence = 0

    pounds += int(input("How many pounds do you have?"))
    pence += int(input("How much pence do you have?"))
    pence = pence / 100
    money = pounds + pence
    print(f"You inserted £{money}")

    if MENU[drink]["cost"] <= money:
        change = money - MENU[drink]["cost"]
        resources["profit"] += money
        print(f"Your change is {change}")
        return True
    elif MENU[drink]["cost"] > money:
        print("Not enough money")
        return False

def make_coffee(drink):
    if "water" in MENU[drink]["ingredients"]:
        resources["water"] -= MENU[drink]["ingredients"]["water"]
    if "milk" in MENU[drink]["ingredients"]:
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    if "coffee" in MENU[drink]["ingredients"]:
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    print(f"Here is your {drink}!")

def coffee_machine():
    machine_on = True
    while machine_on:

        choice  = str(input("What would you like? Espresso, Latte, or Cappuccino?")).lower()
        if choice in MENU:
            if check_resources(choice):
                if check_price(choice):
                    print("Making coffee...")
                    make_coffee(choice)
        elif choice == "off":
            machine_on = False
        elif choice == "report":
            print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}ml\nMoney: £{resources['profit']}")
        else:
            print("input not valid")

# drink = str(input("What drink do you want to make?")).lower()
# check_resources(drink)

coffee_machine()