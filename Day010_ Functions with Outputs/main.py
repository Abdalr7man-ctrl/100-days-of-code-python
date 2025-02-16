from art import logo 

def num1():
    while True :
        num1=input("What's the first number?: ")
        if num1.isdigit():
            return int(num1)
        else : print("Valid input.")

def operation():
    while True :
        operation=input("+\n-\n*\n/\nPick an operation: ")
        if operation in ["+","-","*","/"]:
            return operation
        else : print("Valid input.")

def num2():
    while True :
        num2=input("What's the next number?: ")
        if num2.isdigit():
            return int(num2)
        else : print("Valid input.")


def add(num1,num2):
    print(f"{num1()} {operation} {num2()} = {num1()+num2()}")
    return num1()+num2()

def substract(num1,num2):
    print(f"{num1()} {operation} {num2()} = {num1()-num2()}")
    return num1()-num2()

def multiply(num1,num2):
    print(f"{num1} {operation} {num2} = {num1*num2}")
    return num1*num2

def divide(num1,num2):
    print(f"{num1} {operation} {num2} = {num1/num2}")
    return num1/num2

dict_operations={"*":multiply,"/":divide,"+":add,"-":substract}

print(logo)
num1()
while True :
    print(logo)
    operation()
    num2()
    cont=input(f"Type 'y' to continue calculating with {dict_operations[operation()](num1,num2)}, or type 'n' to start a new calculation: ").lower()
    if cont =="y":
        continue
    elif cont == "n":
        num1=dict_operations[operation](num1,num2)