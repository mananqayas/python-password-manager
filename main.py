from classes import PasswordManager, Password, User
import re

def login():
            pm = PasswordManager()
            correct_email = False
            while correct_email == False:
                email = input("Enter your email address\n")
                regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
                if re.match(regex, email):
                     password = input("Enter your password\n")
                     pm.login(email, password)
                     if pm.logged_in_user:
                         print(f"user logged in as {pm.logged_in_user.email}")
                         logged_in = True
                         while logged_in:
                             print("Please choose from the following:\n")
                             print("Enter \"get-passwords\" to get all of your passwords\n")
                             print("Enter \"create-password\" to create a new password\n")
                             print("Enter \"delete-password\" to delete a password\n")
                             print("Enter \"logout\" to logout\n")
                             ask = input("Choose your option\n")
                             if ask == "get-passwords":
                                 print("=========ALL PASSWORDS=========")
                                 pm.logged_in_user.get_all_passwords()
                                 print("=========ALL PASSWORDS=========")
                                 
                             elif ask == "create-password":
                                 print("----------------------------------------------")
                                 title = input("Enter the password item title\n")
                                 print("----------------------------------------------")
                                 url = input("Enter url of site this password is for\n")
                                 print("----------------------------------------------")
                                 username = input("What is username of this account?\n")
                                 print("----------------------------------------------")
                                 password = input("What is password for this account?\n")
                                 print("----------------------------------------------")
                                 pm.logged_in_user.create_password(title, url, username, password)

                             elif ask == "delete-password":
                                 print("=========ALL PASSWORDS ARE HERE=========")
                                 pm.logged_in_user.get_all_passwords()
                                 print("Please select the title from the above passwords")
                                 title = input("Enter the password item title you want to delete\n")
                                 pm.logged_in_user.delete_password(title)
                             elif ask == "logout":
                                 print("----------------------------------------------")
                                 print("You are logged out successfully! Goodbye")
                                 print("----------------------------------------------")
                                 logged_in = False
                                 exit()
                             else:
                                 print("XXXX Please enter a valid option")
                                
                         correct_email = True
                else:
                    print("Enter a valid email address")

def main():
    onboarding = False
    while onboarding == False:
        print("Welcome to Secure Password Manager App, please select one of the following options\n01: Create an account (enter \"register\")\n02: Login to an exisiting account (enter \"login\")\n")
        option = input("Enter your option\n")
        if(option == "login"):
            login()

            
            onboarding = True
        elif(option == "register"):
            correct_email = False
            while correct_email == False:
                email = input("Enter your email address\n")
                regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
                if re.match(regex, email):
                    password = input("Enter your password\n")
                    pm = PasswordManager()
                    pm.register(email, password)
                    print("Please login")
                    email = input("Enter your email to login\n")
                    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
                    if re.match(regex, email):
                        password = input("Enter your password\n")
                        pm.login(email, password)
                        user = pm.logged_in_user
                        if user:
                            print(f"user logged in as {pm.logged_in_user.email}")
                            logged_in = True
                            while logged_in:
                                print("Please choose from the following:\n")
                                print("Enter \"get-passwords\" to get all of your passwords\n")
                                print("Enter \"create-password\" to create a new password\n")
                                print("Enter \"delete-password\" to delete a password\n")
                                print("Enter \"logout\" to logout\n")
                                ask = input("Choose your option\n")
                                if ask == "get-passwords":
                                    print("=========ALL PASSWORDS=========")
                                    pm.logged_in_user.get_all_passwords()
                                    print("=========ALL PASSWORDS=========")
                                elif ask == "create-password":
                                    print("----------------------------------------------")
                                    title = input("Enter the password item title\n")
                                    print("----------------------------------------------")
                                    url = input("Enter url of site this password is for\n")
                                    print("----------------------------------------------")
                                    username = input("What is username of this account?\n")
                                    print("----------------------------------------------")
                                    password = input("What is password for this account?\n")
                                    print("----------------------------------------------")
                                    pm.logged_in_user.create_password(title, url, username, password)
                                elif ask == "delete-password":
                                    print("=========ALL PASSWORDS ARE HERE=========")
                                    pm.logged_in_user.get_all_passwords()
                                    print("Please select the title from the above passwords")
                                    title = input("Enter the password item title you want to delete\n")
                                    pm.logged_in_user.delete_password(title)
                                elif ask == "logout":
                                    print("----------------------------------------------")
                                    print("You are logged out successfully! Goodbye")
                                    print("----------------------------------------------")
                                    logged_in = False
                                    exit()
                                else:
                                    print("XXXX Please enter a valid option")




                  
                    correct_email = True
                else:
                    print("Not matched")


           
            onboarding = True
        else:
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            print("Please provide a valid option")
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
  
    

if __name__ == '__main__':
    main()




