import random 

list = ["+","-","x","%"]
score = 0
question = 0

print('Welcome to the math game application...')
print('Please do the operations without using a calculator...')
print('The application will remain open until 10 questions are answered correctly...')

while(score < 10):

    math = random.choice(list)

    if(math == "+"):

        number1 = random.randint(0,1000)
        number2 = random.randint(0,1000)
        answer = number1 + number2

        user_answer = int(input(f"{number1} + {number2}\nWhat is the result of this?"))

        if(answer == user_answer):

            print("That's correct. Congrats.")
            score += 1
            question += 1

        else:

            print(f"That's incorrect. The correct answer is {answer}")
            question += 1

    elif(math == "-"):

        number1 = random.randint(0,1000)
        number2 = random.randint(0,1000)

        if(number1 > number2):

            answer = number1 - number2

            user_answer = int(input(f"{number1} - {number2}\nWhat is the result of this?"))

            if(answer == user_answer):

                print("That's correct. Congrats.")
                score += 1
                question += 1

            else:

                print(f"That's incorrect. The correct answer is {answer}") 
                question += 1   

        else:

            answer = number2 - number1

            user_answer = int(input(f"{number2} - {number1}\nWhat is the result of this?"))

            if(answer == user_answer):

                print("That's correct. Congrats.")
                score += 1
                question += 1

            else:

                print(f"That's incorrect. The correct answer is {answer}")    
                question += 1

    elif(math == "x"):

        number1 = random.randint(0,1000)
        number2 = random.randint(0,1000)
        answer = number1 * number2

        user_answer = int(input(f"{number1} x {number2}\nWhat is the result of this?"))

        if(answer == user_answer):

            print("That's correct. Congrats.")
            score += 1
            question += 1

        else:

            print(f"That's incorrect. The correct answer is {answer}")    
            question += 1    

    else:
                    
        number1 = random.randint(0,1000)
        number2 = random.randint(0,1000)

        if(number1 > number2):
            
            answer = number1 // number2

            user_answer = int(input(f"{number1} % {number2}\nWhat is the result of this operation as an integer?"))

            if(answer == user_answer):

                print("That's correct. Congrats.")
                score += 1
                question += 1

            else:

                print(f"That's incorrect. The correct answer is {answer}")    
                question += 1

        else:
            
            answer = number2 // number1

            user_answer = int(input(f"{number2} % {number1}\nWhat is the result of this operation as an integer?"))

            if(answer == user_answer):

                print("That's correct. Congrats.")
                score += 1
                question += 1

            else:

                print(f"That's incorrect. The correct answer is {answer}")   
                question += 1

print(f"You have {score} correct answer out of {question} questions.") 