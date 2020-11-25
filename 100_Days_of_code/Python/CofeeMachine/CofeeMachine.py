#/usr/bin/python3

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
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

coins = {
    "quarter": 0.0,
    "dime": 0.0,
    "nickel": 0.0,
    "penny": 0.0,
}


def print_options():
    return input("What would you like? (espresso/latte/cappuccino): ")


def actions(action):
    if action == "report":
        report()
    elif action != "off":
        if check_ingredients(action):
            print("Please insert coins.")
            get_coins()
            check_transaction(action)


def get_coins():
    for key in coins:
        coins[key] = float(input(f"How many {key}?: "))


def check_transaction(action):
    cost = MENU[action]["cost"]
    having = round(coins["quarter"] * 0.25 + coins["dime"] * 0.10 + coins["nickel"] * 0.05 + coins["penny"] * 0.01, 2)
    print(f"Cost: {cost}, Having: {having}")

    if having < cost:
        print("Sorry that's not enough money. Money refunded.")
    else:
        if having > cost:
            print(f"Here is your {having - cost} in exchange.")
        print(f"Here is your {action} ☕. Enjoy!")
        add_revenue(action)
        release_materials(action)


def add_revenue(action):
    resources["money"] += MENU[action]["cost"]


def release_materials(action):
    for key in MENU[action]["ingredients"]:
        resources[key] -= MENU[action]["ingredients"][key]


def report():
    for key in resources:
        magnitude = "ml"
        mark = ""
        if key == "coffee":
            magnitude = "g"
        elif key == "money":
            mark = "$"
            magnitude = ""
        print(f"{key}: {mark}{resources[key]}{magnitude}")


def check_ingredients(choice):
    enough = False
    ingredients = MENU[choice]
    for key in ingredients["ingredients"]:
        if int(resources[key]) >= int(ingredients["ingredients"][key]):
            enough = True
        else:
            print(f"Sorry there is not enough {key}.")
            return False
    return enough


option = ""
while option != "off":
    option = print_options()
    actions(option)
print("Shutting down")

