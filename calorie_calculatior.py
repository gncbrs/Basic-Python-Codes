#coded by Gonenc Baris Bezik
print("-----Calorie Calculator-----")

#In here we calculate the total amount of calorie for woman.
def calorie_for_woman():
    #BMR (kcal / day)= 10 × weight (kg) + 6.25 × height (cm) – 5 × age (y) – 161 (kcal / day).
    weight = float(input("Enter your weight(kg): "))
    height = float(input("Enter your height(cm): "))
    age = int(input("Enter your age(year): "))

    BMR = (10 * weight) + (6,25 * height) - (5 * age) - 161

    #And now we have to learn what does this person want. Lose, gain, or protect his/er weight.
    lose_protect_gain = input("Do you want to lose(l), protect(p), or gain(g) weight: ").lower()

    if lose_protect_gain == "l" or lose_protect_gain == "lose":
        BMR -= (BMR * 20) / 100
        print(f"You should take {BMR} calories per day for lose weight.")

    elif lose_protect_gain == "p" or lose_protect_gain == "protect":
        print(f"You should take {BMR} calories per day for protect weight.")

    elif lose_protect_gain == "g" or lose_protect_gain == "gain":
        BMR += (BMR * 20) / 100
        print(f"You should take {BMR} calories per day.")

    else:
        print("Invalid entered, please try again...")

#In here we calculate the total amount of calorie for man.
def calorie_for_man():
    #BMR (kcal / day) = 10 × weight (kg) + 6.25 × height (cm) – 5 × age (y) + 5 (kcal / day).
    weight = float(input("Enter your weight(kg): "))
    height = float(input("Enter your height(cm): "))
    age = int(input("Enter your age(year): "))

    BMR = (10 * weight) + (6.25 * height) - (5 * age) - 5

    #And now we have to learn what does this person want. Lose, gain, or protect his/er weight.
    lose_protect_gain = input("Do you want to lose(l), protect(p), or gain(g) weight: ").lower()

    if lose_protect_gain == "l" or lose_protect_gain == "lose":
        BMR -= (BMR * 20) / 100
        print(f"You should take {BMR} calories per day for lose weight.")

    elif lose_protect_gain == "p" or lose_protect_gain == "protect":
        print(f"You should take {BMR} calories per day for protect weight.")

    elif lose_protect_gain == "g" or lose_protect_gain == "gain":
        BMR += (BMR * 20) / 100
        print(f"You should take {BMR} calories per day.")

    else:
        print("Invalid entered, please try again...")

#Now we have to start our application.
while True:
    y_or_n = input("Do you want to calculate your calorie(y/n): ").lower()

    if y_or_n == "y" or y_or_n == "yes":
        m_or_w = input("If you are a man enter 'm'. If you are a woman enter 'w': ").lower()

        if m_or_w == "m" or m_or_w == "man":
            calorie_for_man()

        elif m_or_w == "w" or m_or_w == "woman":
            calorie_for_woman()

        else:
            print("You entered invalid value, please try again...")

    elif y_or_n == "n" or y_or_n == "no":
        print("If you want to calculate I am always here and waiting you.")
        print("Have a nice day...")
        break

    else:
        print("Invalid value, please try again...")
