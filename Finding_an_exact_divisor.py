while True:
    user_number = input("Enter a positive number or exit to 'q': ").lower()

    if(user_number == "q"):
        print("Okay Goodbye.")
        break

    else:

        try:
            number = int(user_number)

            for num in range(1,number + 1):

                if(number % num == 0):
                    print("The divisors of this number: ",num)

        except:
            print("Something went wrong. Please enter a number.")