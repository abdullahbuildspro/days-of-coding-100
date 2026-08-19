
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
}

rot = True

def compare_resources(coffee):
    orders = MENU[coffee]["ingredients"]
    global item
    for item, amount in orders.items():
        if resources[item] < amount:
            print(f"Sorry, there is not enough {item}.")
            return False
    for item, amount in orders.items():
        resources[item] -= amount
    return True


def check_currencies(quarters, dimes, nickles, pennies):
    total10 = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    if total10 == MENU[order]["cost"]:
        return "Here is your latte ☕️. Enjoy!"
    elif total10 > MENU[order]["cost"]:
        rest = round(total10 - MENU[order]["cost"], 1)
        global num1
        num1 += float(round(MENU[order]["cost"], 1))
        print(f"Here is ${rest} in change.")
        return f"Here is your {order} ☕️. Enjoy!"
    else:
        return "Sorry that's not enough money. Money refunded."

num1 = 0

while rot:

    money = f"${num1}"
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order == "report":
        resources["Money"] = money
        for i in resources:
            print(f"{i}: {resources[i]}")


    elif order == "off":
        rot = False

    elif order == "espresso" or order == "latte" or order == "cappuccino":
        if compare_resources(order):
            print("Please insert coins.")
            quarter = int(input("how many quarters?: "))
            dime = int(input("how many dimes?: "))
            nickle = int(input("how many nickles?: "))
            pennie = int(input("how many pennies?: "))

            print(check_currencies(quarter, dime, nickle, pennie))

        else:
            rot = False
    else:
        print("Please enter the correct information.")
        rot = False
