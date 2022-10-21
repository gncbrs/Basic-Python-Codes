print("""
***************************************
Geometry Machine;

Process 1: Triangle Calculation

Process 2: Exit
***************************************
""")

while True:
    process = input("Enter a process: ")
    
    if (process == "2"):
        print("Sign out.")
        break

    elif (process == "1"):
        print("Okay now enter 3 numbers: ")
        
        try:
            x = float(input("Enter a number: "))
            y = float(input("Enter a number: "))
            z = float(input("Enter a number: "))
            
            u = (x + y + z) / 2 # Required to calculate area

            print("The area according to these numbers: {}".format((u*(u-x)*(u-y)*(u-z))**(1/2)))

        except:
            print("Error detected.")
        
    else:
        print("Please enter a valid process.")