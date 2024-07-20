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


def is_resource_sufficient(order_ingredients):
    """Returns true when order can be made, False if ingredients are sufficient"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            is_enough = False
    return is_enough


def process_coins():
    """Returns total from calculated from coins inserted"""
    print("Please enter coins.")
    total = int(input("How many quarters?:")) * 0.25
    total += int(input("How many dimes?:")) * 0.1
    total += int(input("How many nickles?:")) * 0.05
    total += int(input("How many pennies?:")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns true when money is accepted, and false when money is not sufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is {change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that is not enough money,money refunded")
        return False


def make_coffee(drink_name, order_ingredient):
    """Deduct required ingredients from the resources"""
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"Here is your {drink_name} ☕")


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffe: {resources['coffee']}gm")
        print(f"money: $2.5"),
    else:
        drink = MENU[choice]
        print(drink)
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink["ingredients"])
