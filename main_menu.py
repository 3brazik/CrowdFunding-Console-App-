from user_validation_function import *
from login import *
from registration import*

# signup or login function 

def register():
    print("\n*************************************************************************************\n")
    print("\t\t\tWelcome to Crowd-Funding Console App")
    print("\n*************************************************************************************\n")
    print(" Select one of the following options :- \n")
    choice = int(
        input("\t1) Please Enter 1 to login \n\t2) Please Enter 2 to Signup \n "))
    try:
        choice == 1 or choice == 2
    except:
        print("<ERROR> Please Enter 1 to login  or 2 to signUp ")
    else:
        if choice == 1:
            try:
                login()
            except:
                print(" <ERROR> Something went wrong")
        elif choice == 2:
            try:
                registration()
            except:
                print(" <ERROR> Something went wrong")
        else:
            print(" <ERROR> Invalid Choice")

register()
