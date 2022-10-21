import time

print("Welcome my quiz game.")

start = input("Do you want to play? ").lower()

point = 0

if (start == "yes"):
    print("Okay let's start.")

    answer = input("What does CPU stand for? ").lower()

    if (answer == "central procress unit"):
        time.sleep(1)
        print("Correct!")
        point += 1

    else:
        time.sleep(1)
        print("Incorrect!")
    
    answer2 = input("What does GPU stand for? ").lower()
    
    if (answer2 == "graphics processing unit"):
        time.sleep(1)
        print("Correct!")
        point += 1

    else:
        time.sleep(1)
        print("Incorrect!")

    answer3 = input("What does RAM stand for? ").lower()
    
    if (answer3 == "random access memory"):
        time.sleep(1)
        print("Correct!")
        point += 1

    else:
        time.sleep(1)
        print("Incorrect!")
    
    answer3 = input("What does PSU  stand for? ").lower()
    
    if (answer3 == "power supply unit"):
        time.sleep(1)
        print("Correct!")
        point += 1

    else:
        time.sleep(1)
        print("Incorrect!")


    print("You got " + str(point) + " questions correct!")

else: 
    print("Okay")
