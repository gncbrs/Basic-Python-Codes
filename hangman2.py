#Coded by Gönenç Barış Bezik
#Please use this document with words.txt
import random

#Word selection section.
def get_word():
    
    with open("words.txt","r") as f:
        words = f.read().splitlines()
   
    return random.choice(words)

#Coding the application.
def hangman():
    choosen_word = get_word()
    display = []
    
    for _ in choosen_word:
        display += "_"
    
    lives = 0

    print("Welcome to Hangman Game")
    difficulty = input("Entern a diffucilty level(baby, normal, hard): ")

    if difficulty == "baby":
        lives = len(choosen_word) * 3
        print("Guess the word:- ", end=" ")
        print(f"{' '.join(display)}")
        print(f"Lives: {lives}")

        while True:
            guess = input("Guess a letter: ").lower()

            if not guess in choosen_word:
                print("Wrong guess...")
                lives -= 1

            index = 0

            for i in choosen_word:
                if guess == i:
                    display[index] = guess

                index += 1

            print(f"{' '.join(display)}")
            print(f"Lives: {lives}")     

            if "_" not in display:
                print("You won...")
                break

            if lives == 0:
                print("You lose...")
                print(f"Choosen word is {choosen_word}")
                break

    elif difficulty == "normal":
        lives = len(choosen_word) * 2
        print("Guess the word:- ", end=" ")
        print(f"{' '.join(display)}")
        print(f"Lives: {lives}")

        while True:
            guess = input("Guess a letter: ").lower()

            if not guess in choosen_word:
                print("Wrong guess...")
                lives -= 1

            index = 0

            for i in choosen_word:
                if guess == i:
                    display[index] = guess

                index += 1

            print(f"{' '.join(display)}")
            print(f"Lives: {lives}")     

            if "_" not in display:
                print("You won...")
                break

            if lives == 0:
                print("You lose...")
                print(f"Choosen word is {choosen_word}")
                break

    elif difficulty == "hard":
        lives = len(choosen_word) 
        print("Guess the word:- ", end=" ")
        print(f"{' '.join(display)}")
        print(f"Lives: {lives}")

        while True:
            guess = input("Guess a letter: ").lower()

            if not guess in choosen_word:
                print("Wrong guess...")
                lives -= 1

            index = 0

            for i in choosen_word:
                if guess == i:
                    display[index] = guess

                index += 1

            print(f"{' '.join(display)}")
            print(f"Lives: {lives}")     

            if "_" not in display:
                print("You won...")
                break

            if lives == 0:
                print("You lose...")
                print(f"Choosen word is {choosen_word}")
                break

    else:
        print("Your answer is invalid...")
        print("Please enter a valid input.")

while True:
    ask = input("Do you want to play Hangman? (y/n): ").lower()
    
    if ask == 'y' or ask == 'yes':
        hangman()
    
    elif ask == 'n' or ask == 'no':
        print("Good bye...")
        break
    
    else:
        print("Your answer is invalid...")
        print("Please enter a valid input.")
