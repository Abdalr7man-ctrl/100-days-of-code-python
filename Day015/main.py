"""
Coffee Machine
"""
from machine import MENU, resources

def your_money():
    print("Please insert coins.")

    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01

    global money
    money = quarters + dimes + nickles + pennies
    return money

def report():
    print()
    for i in resources:
        print(f"{i}: {resources.get(i)}")
    print()

def asking_drink():
    drink = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if drink in ["espresso", "latte", "cappuccino"]:
        return drink

    elif drink == "off":
        return False

    elif drink == "report":
        report()
        return asking_drink()

    else:
        print("Invalid input.")
        return asking_drink()

def choose():
    """Check the user's input to decide what to do next."""

    global choice
    choice = asking_drink()

    if not choice:
        return None

    global ingredients
    ingredients = MENU.get(choice).get("ingredients")

    for item in ingredients:

        if ingredients[item] > resources[item]:
            print(f"\nSorry there is not enough {item}.\n")
            return choose()

    your_money()
    if money < MENU.get(choice).get("cost"):
        print("\nSorry there is not enough money.\n")
        return choose()
    elif money > MENU.get(choice).get("cost"):
        print(
            f"Here is ${round((money - MENU.get(choice).get('cost')), 2)} dollars in change."
        )

    transaction()
    print(f"\nHere is your {choice}. Enjoy!\n")
    return choose()

def transaction():

    for item in ingredients:
        resources[item] -= ingredients[item]

if __name__ == "__main__":

    choose()
