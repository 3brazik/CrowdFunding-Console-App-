import re



# vaildate name and checking regex
def validate_name():
    print("***************************************************************************\n")
    first_name = input(" Please Enter your First Name :  ").strip().lower()
    while True:
        if first_name.isalpha():
            last_name = input(" Please Enter your Last name :   ").strip().lower()
            if last_name.isalpha():
                break
            else:
                print(" <NAME_ERROR> Last Name Cannot Contain Spaces or Digits ")
        elif first_name.isspace() or first_name.isalnum():
            print(" <NAME_ERROR> First Name Cannot Contain Spaces or Digits !")
            first_name = input(" Please Enter your First Name :  ").strip().lower()
    return [first_name, last_name]

# validate email and checking regex
def validate_email():
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.com\b'
    email = input(" Please Enter your E-mail  ").strip().lower()
    while True:
        if(re.fullmatch(regex, email)):
            break
        else:
            print(" <E-mail_ERROR> Invalid Email")
            email = input(" Please Enter Valid E-mail Contains @ and .com : ").strip().lower()
    return email

# validate password function 
def validate_password():
    regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$'
    password = input(" NOTE--> Password should contain...\n -lowercase, uppercase, number,special-char and should be at least 8 char \n Please Enter Your Password ").strip()
    while True:
        if(re.fullmatch(regex, password)):
            pass_confirm = input(" Please Enter password again : ").strip()
            if password != pass_confirm:
                print(" <Password_ERROR> Please confirm  your password , they are not the same")
            else:
                break
        else:
            print("Invalid password")
            password = input(
                " Please Enter valid Password \n Password should contain...\n -lowercase, uppercase, number,special-char and should be at least 8 ").strip().lower()
    return password

# validate Phone Number function
def validate_phone():
    phone = input("Note --> Enter 11 Digits Starts [validated against Egyptian phone numbers] \n Please enter your number : ").strip().lower()
    while True:
        if len(phone) == 11 and phone.isnumeric():
            break
        else:
            print(" <ERROR> Please Enter a Valid Egyptian Number ")
            phone = input("Enter 11 Digits Starts [validated against Egyptian phone numbers] \n Please enter your number :  ").strip().lower()
    return phone


