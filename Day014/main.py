import random

from art import logo, vs
from game_data import data

def random_guy():
    """its return random choice from game_data.py file"""
    return random.choice(data), random.choice(data)

def game():
    score = 0
    choice1, choice2 = random_guy()
    while True :
        if choice1["follower_count"] > choice2["follower_count"] :
            choice2 = choice1
        else :
            choice1 = choice2
        while choice2 == choice1 :
            choice2 = random_guy()[1]
        guy1 = f"Compare A: {choice1['name']}, a {choice1['description']},from {choice1['country']}"
        guy2 = f"Compare B: {choice2['name']}, a {choice2['description']}, from {choice2['country']}"
        print(logo)
        print(guy1)
        print(vs)
        print(guy2)
        choice = input("\nWho has more followers? Type 'A' or 'B': \n").lower()
        if(
            choice == "a" 
            and choice1['follower_count'] > choice2['follower_count']
            or choice == "b" 
            and choice1['follower_count'] < choice2['follower_count']
            ):
            score += 1 
            print(f"You're right! Current score: {score}.")

        elif(
            choice == "a"
            and choice1['follower_count'] < choice2['follower_count']
            or choice == "b"
            and choice1['follower_count'] > choice2['follower_count']
            ):
            print(f"Sorry, that's wrong. Final score: {score}")
            break

        else:
            print("Invalid input, please try again.")

while True :
    game()
    if input("Do You Want to play again(y/n)? ") == "y" :
        continue
    break
