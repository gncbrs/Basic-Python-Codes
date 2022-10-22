import time

def is_it_prime(number):
    
    if (number == 1):
        return False
    
    elif (number == 2):
        return True
    
    else:
        for i in range(2,number):
            if (number % i == 0):
                return False
        return  True

while True:
    number = input("Please enter a number or 'q' to exit: ")

    if number == "q":
        print("Exit.")
        break
    
    else:

        try:

            number = int(number)

            if (is_it_prime(number)):
                print("Calculating...")
                time.sleep(1)
                print(number,"is a prime number.")

            else:
                print("Calculating...")
                time.sleep(1)
                print(number,"is not a prime number.")
        
        except:
            print("Error detected.")