from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

myCoffeeMaker = CoffeeMaker()
myMenu = Menu()
myMoneyMachine = MoneyMachine()

def check_resources(drink: str, ):
    drink_object = myMenu.find_drink(drink)
    return myCoffeeMaker.is_resource_sufficient(drink_object)

def check_cost(drink: str):
    drink_object = myMenu.find_drink(drink)
    return myMoneyMachine.make_payment(drink_object.cost)

def make_order(drink: str):
    drink_object = myMenu.find_drink(drink)
    myCoffeeMaker.make_coffee(drink_object)

def main():

    while True:
        choose = input("What would you like?:\n"\
                    "1-espresso\n"
                    "2-latte\n"
                    "3-cappuccino\n"
                    "4-report\n")
        drinks = ["espresso", "latte", "cappuccino"]
        if choose in ["1", "2", "3"]:
            drink = drinks[int(choose) - 1]
            if not check_resources(drink):
                continue
            if not check_cost(drink):
                continue
            make_order(drink)

        elif choose == "4":
            myCoffeeMaker.report()
        elif choose == "off":
            break
        else:
            print("\nInValid Choice.\n")


if __name__ == "__main__":

    try:
        main()
    except KeyboardInterrupt:
        print("\n" * 50)
