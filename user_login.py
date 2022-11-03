from getpass import getpass

sys_user_name = getpass("Create a user name: ")
sys_password = getpass("Create a password: ")

right_to_try = 3

while True:
    user_name = input("Enter your user name: ")
    password = input("Enter your password: ")

    if(user_name == sys_user_name and password == sys_password):
        print("logging in")
        break

    if(right_to_try == 0):
        print("You entered too many wrong entries, try again later")
        break
    
    else:
        print("User name or password incorrect")
        right_to_try -= 1