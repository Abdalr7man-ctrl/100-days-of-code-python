from art import logo 

def num1fun():
    global num1
    while True :
        num1=input("What's the first number?: ")
        if num1.isdigit():
            num1=int(num1)
            break
        print("Valid input.")

def operationfun():
    global operation
    while True :
        operation=input("+\n-\n*\n/\nPick an operation: ")
        if operation in ["+","-","*","/"]:
            return operation
        print("Valid input.")

def num2fun():
    global num2
    while True :
        num2=input("What's the next number?: ")
        if num2.isdigit():
            num2=int(num2)
            break
        print("Valid input.")

def add(num1,num2):
    return num1+num2

def substract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

dict_operations={"*":multiply,"/":divide,"+":add,"-":substract}

print(logo)
num1fun()
while True :
    print(logo) 
    operationfun()   # TODO : Handling ZeroDivisionError 
    num2fun()  
    print(f"{num1} {operation} {num2} = {dict_operations[operation](num1,num2)}")
    cont=input(f"Type 'y' to continue calculating with {dict_operations[operation](num1,num2)}, or type 'n' to start a new calculation: ").lower()
    if cont =="y":
        num1=dict_operations[operation](num1,num2)
        continue
    elif cont == "n":
        break