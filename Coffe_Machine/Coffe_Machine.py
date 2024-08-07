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

def check_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Profit: ${profit}")

def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


def process_order(user_choice):
    global profit
    order = MENU[user_choice]
    if is_resources_sufficient(order["ingredients"]):
        payment = process_coins()
        if payment >= order["cost"]:
            change = round(payment - order["cost"], 2)
            profit += order["cost"]
            for item in order["ingredients"]:
                resources[item] -= order["ingredients"][item]
            print(f"Here is your {user_choice}. Enjoy!")
            if change > 0:
                print(f"Here is ${change} in change.")
        else:
            print("Sorry, that's not enough money. Money refunded.")
    else:
        print("Order could not be processed due to insufficient resources.")



def coffee_machine():
    while True:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_choice == "report":
            check_report()
        elif user_choice == "off":
            print("Turning off the coffee machine.")
            break
        elif user_choice in MENU:
            process_order(user_choice)
        else:
            print("Invalid choice. Please choose a valid option.")

coffee_machine()
