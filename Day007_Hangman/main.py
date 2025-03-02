from art import *
import random 

word_list=('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

chosen_word=random.choice(word_list)

correct_letter=[]
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

life=6
counter=0
print(logo3)
print("-"*len(chosen_word))

while True :
    
    unknow_word=""
    
    guess=input("Guess a letter : ").lower()
    
    for i in chosen_word :
    
        if i == guess:
            unknow_word+=i
            correct_letter.append(i)
        elif i in correct_letter:
            unknow_word+=i
        else :
            unknow_word+="-"

    if guess not in unknow_word:
        life-=1
        counter+=1
        print("**************** wrong char :) ****************")
    
    print(unknow_word)
    
    print(f"******you still have {life} tries.******")

    print(HANGMANPICS[counter])

    if not "-" in unknow_word :
        print(logo2)
        break
    elif life == 0: 
        print("you lose :(")
        break