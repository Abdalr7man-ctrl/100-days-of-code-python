from game_data import data
from art import * 
import random

def random_guy():
    return [random.choice(data), random.choice(data)]

def game():
    score = 0
    while True :
        choise1 = random_guy()[0]
        choise2 = random_guy()[1]
        guy1 = f"Compare A: {choise1['name']}, a {choise1['description']}, from {choise1['country']}"
        guy2 = f"Compare B: {choise2['name']}, a {choise2['description']}, from {choise2['country']}"
        print(logo)
        print(guy1)
        print(vs)
        print(guy2)
        choise = input("\nWho has more followers? Type 'A' or 'B': \n").lower()
        
        if choise == "a" and choise1['follower_count'] > choise2['follower_count']\
        or choise == "b" and choise1['follower_count'] < choise2['follower_count'] :
            score += 1 
            print(f"You're right! Current score: {score}.")
        
        elif choise == "a" and choise1['follower_count'] < choise2['follower_count']\
        or choise == "b" and choise1['follower_count'] > choise2['follower_count'] :
            print(f"Sorry, that's wrong. Final score: {score}")
            break
        
        else :
            print("Valid input.")

game()
