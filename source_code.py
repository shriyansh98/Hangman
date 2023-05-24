import random
import word
import os 

from word import hangman_words
from hm_art import logo , stages

game_exit = False

while not game_exit :
    word = random.choice(hangman_words)
    #print(f"choosen letter is {word}")

    blanks = []
    lenght_word = 0
    for letters in word:
        blanks += "_"
        lenght_word += 1

    end_of_game = False
    lives = 6

   

    print(logo)
    print("\n")
    print("      P:PLAY      E: EXIT     \n")
    ans= input().upper()
    if ans == "P":
        #os.system('clear')       
        os.system('cls' if os.name == 'nt' else 'clear')

    elif ans == "E":
        break

    #while not end_of_game:
    #print("new screen")
    while not end_of_game:
        if lives==6:
            print(stages[7],"\n")
            print(f"{' '.join(blanks)}\n")

        guess = input("Guess a letter: ").lower()

        os.system('cls' if os.name == 'nt' else 'clear')

        if guess in blanks:
            print(f"letter already guessed {guess}")
        
        for letters in range(lenght_word):
            letter = word[letters]
            if letter == guess:
                blanks[letters]=letter

        if guess not in word:
            print(f"{guess} is not in the word")

            lives -=1
            if lives == 0 :
                end_of_game = True
                print ("YOU LOOSE")

        print(f"{' '.join(blanks)}")

        if '_' not in blanks:
            end_of_game = True
            print("YOU WIN")

       
        print(stages[lives])

print("Thanks for playing")
