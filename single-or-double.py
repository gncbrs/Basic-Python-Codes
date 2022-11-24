import time

def single_double(number):

    if (number < 0):
        print("Negative numbers are not calculated as odd or even.")

    elif (number % 2 == 0):
        print("This is a Double Number.")

    elif (number % 2 != 0):
        print("This is a Single Number.")

while True:

    try:
        num = input("Enter a number or 'q' to exit: ").lower()

        if num == "q":
            print("bye bye")
            time.sleep(1)
            break

        else:
            number = int(num)
            single_double(number)      

    except:
        print("Something went wrong.")
