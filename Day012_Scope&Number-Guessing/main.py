import random
from art import logo

def game():

    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    num = random.randrange(0,101) 

    if difficulty == "easy" :
        
        chance = 10
        
        while chance > 0 :
            print(f"You have {chance} attempts remaining to guess the number.")
            guess = input("Make a guess: ")
            while not guess.isdigit() :
                guess = input("Make a guess: ")
            
            if int(guess) == num :
                print(f"you got it the number is {num}")
                break
            else :
                chance -= 1
                if num > int(guess) :
                    print("Too low")
                else :
                    print("Too hight")
        else :
            print("You've run out of guesses. Refresh the page to run again.")

    else :

        chance = 5
        
        while chance > 0 :
            print(f"You have {chance} attempts remaining to guess the number.")
            guess = input("Make a guess: ")
            while not guess.isdigit() :
                guess = input("Make a guess: ")
            
            if int(guess) == num :
                print(f"you got it the number is {num}")
                break
            else :
                chance -= 1
                if num > int(guess) :
                    print("Too low")
                else :
                    print("Too hight")
        else :
            print("You've run out of guesses. Refresh the page to run again.")


game()
