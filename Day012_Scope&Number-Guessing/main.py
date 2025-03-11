import random
from art import logo

def get_guess():
    global guess 
    guess = input("Make a guess: ")
    while not guess.isdigit() :
        guess = input("Make a guess: ")

def intro():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    num = random.randrange(1,101) 
    chance = 10 if difficulty == "easy" else 5
    return chance, num

def game():
    chance, num = intro()
    while chance > 0 :
        print(f"You have {chance} attempts remaining to guess the number.")
        get_guess()
        if int(guess) == num :
            print(f"you got it the number is {num}")
            break
        elif int(guess) not in range(1,101) :
            print("Out of range 1->100 Try again.")
        else :
            chance -= 1
            if num > int(guess) :
                print("Too low")
            else :
                print("Too high")
    else :
        print("You've run out of guesses Game Over.")

while True :
    game()
    again = input("would you want to play again? y or n ")
    if again.lower() == "y" :
        continue
    else :
        break