from art import logo
print(logo)

People_involved={}
others=True

while others:
    name=input("What's your name?: ")

    bid=input("What's your bid: $")
    while not bid.isdigit():
        print("Valid in put put number.")
        bid=input("What's your bid: $")

    others=input("Are there any other bidders? Type 'yes' or 'no'.\n ")
    if others =="yes":
        People_involved[name]=bid
        print("\n"*100)
        print(logo)
    else:
        People_involved[name]=bid
        break # break == others=False 

print(f"The wineer is {max(People_involved)} with a bid of ${max(People_involved.values())}")


