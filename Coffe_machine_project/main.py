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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def adequet_resource(order_ingredient):
    """Return True when the order are made, Return False if ingredient are insufficient."""
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coin():
    """Return the total calculated from inserted."""
    print("please insert coin")
    total = int(input("How many quater?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nikles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def transection_successful(money_received, drink_cost):
    """Return True if the payment is accepted, False if money is inadequate."""
    if money_received >=drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here is your change: ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffe(drink_name, order_ingredient):
    """Deduct the required ingredients from the resourece"""
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"Here is your drink {drink_name} ☕")

is_on = True
while is_on:
    choices = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choices == 'off':
        is_on = False
    elif choices == 'report':
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}ml")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choices]
        if adequet_resource(drink['ingredients']):
            payment = process_coin()
            if transection_successful(payment, drink['cost']):
                make_coffe(choices, drink["ingredients"])

