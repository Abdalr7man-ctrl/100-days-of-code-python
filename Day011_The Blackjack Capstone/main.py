import random
from art import logo 

cards = [11,2,3,4,5 ,6,7,8,9,10,10,10,10]
game = "y"
while game == "y":

    game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if game == "y":
        print("\n"*30)
        print(logo)
        card1 =  random.choice(cards)
        card2 = random.choice(cards)
        print(f"Your cards: {[card1,card2]}, current score: {card1+card2}")
        card_compu1 = random.choice(cards)
        print(f"Computer's first card: {card_compu1}")
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")

        if another_card == "y":
            card3 = random.choice(cards)
            print(f"Your final hand: {[card1,card2,card3]}, final score: {card1+card2+card3}")
            card_compu2 = random.choice(cards)
            card_compu3 = random.choice(cards)
            print(f"Computer's final hand: {[card_compu1 , card_compu2 , card_compu3]}, final score: {card_compu1+card_compu2+card_compu3}")

            if 21 >= card1+card2+card3 > card_compu1+card_compu2+card_compu3\
                or card1+card2+card3 > card_compu1+card_compu2+card_compu3 > 21\
                or card1+card2+card3 < 21 < card_compu1+card_compu2+card_compu3  :
                print("You Win")
            elif card1+card2+card3 < card_compu1+card_compu2+card_compu3 <= 21\
                or 21 < card1+card2+card3 < card_compu1+card_compu2+card_compu3\
                or card1+card2+card3 > 21 > card_compu1+card_compu2+card_compu3:
                print("You Lose")
            else :
                print("Draw")

        else :
            print(f"Your final hand: {[card1,card2]}, final score: {card1+card2}")
            card_compu2 = random.choice(cards)
            card_compu3 = random.choice(cards)
            print(f"Computer's final hand: {[card_compu1 , card_compu2 , card_compu3]}, final score: {card_compu1+card_compu2+card_compu3}")

            if 21 >= card1+card2 > card_compu1+card_compu2+card_compu3\
                or card1+card2 > card_compu1+card_compu2+card_compu3 > 21\
                or card1+card2 < 21 < card_compu1+card_compu2+card_compu3  :
                print("You Win")
            elif card1+card2 < card_compu1+card_compu2+card_compu3 <= 21\
                or 21 < card1+card2 < card_compu1+card_compu2+card_compu3\
                or  card1+card2 > 21 > card_compu1+card_compu2+card_compu3 :
                print("You Lose")
            else :
                print("Draw")
    else :
        break