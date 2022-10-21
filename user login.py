print("""
*******************
User Login Program
*******************
""")

sys_user_name = input("Create a user name: ")
sys_password = input("Create a password: ")
right_of_entry = 3

while True:
    user_name = input("Enter a user name: ")
    password = input("Enter a password: ")

    if (user_name == sys_user_name and password != sys_password):
        print("Password is wrong.")
        right_of_entry -= 1

    elif (user_name != sys_user_name and password == sys_password):
        print("User name is wrong.")
        right_of_entry -= 1

    elif (user_name != sys_user_name and password != sys_password):
        print("Both of them are wrong.")
        right_of_entry -= 1

    else:
        print("User Login Successful.")
        break

    if (right_of_entry == 0):
        print("Your Entry Right Has Expired.")
        break