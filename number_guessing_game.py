import time 
import random

print(""" 
***********************************************
Number Guessing Game;
You must guess a number btween 1-100.
You have 5 attempts.
***********************************************
""")

random_number = random.randint(1,100)
attempts = 5

while True: 
    guess = input("Please write your guess or Q for quit: ").lower()

    if (guess == "q"):
        print("Okay goodbye!")
        break

    if (int(guess) == random_number):
        print("Congratulations you won")
        break

    elif (int(guess) <= random_number):
        print("Enter a larger number.")
        attempts -= 1

    elif (int(guess) >= random_number):
        print("Enter a smaller number.")
        attempts -= 1

    if (attempts == 0):
        print("Your attempts are done.Random number was {}".format(random_number))
        break