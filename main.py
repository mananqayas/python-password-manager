from classes import User, PasswordManager, Password
import re
# This function is called when user selects login while interacting with our program
def login():
            pm = PasswordManager()
            correct_email = False
            while correct_email == False:
                email = input("Enter your email address\n")
                regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
                # verifiying email
                if re.match(regex, email):
                     password = input("Enter your password\n")
                     pm.login(email, password)
                     #pm.login returns user state and we are checking if user object was created after logging in, if its None, else block is executed
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
                             # When user enters get-password
                             if ask == "get-passwords":
                                 print("=========ALL PASSWORDS=========")
                                 pm.logged_in_user.get_all_passwords()
                                 print("=========ALL PASSWORDS=========")

                            # When user enters create-password
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
                            
                            # When user enters delete-password
                             elif ask == "delete-password":
                                 print("=========ALL PASSWORDS ARE HERE=========")
                                 pm.logged_in_user.get_all_passwords()
                                 print("Please select the title from the above passwords")
                                 title = input("Enter the password item title you want to delete\n")
                                 pm.logged_in_user.delete_password(title)

                             # When user enters logout
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

# Main function starts running when our program starts, it uses while loops to keep asking the user correct inputs until he gets it right.
def main():
    onboarding = False
    while onboarding == False:
        print("Welcome to Secure Password Manager App, please select one of the following options\n01: Create an account (enter \"register\")\n02: Login to an exisiting account (enter \"login\")\n")
        option = input("Enter your option\n")
        if option == "login":
            login()
        elif option == "register":
            pm = PasswordManager()
            correct = False
            while not correct:
                print("-----------------------------------")
                email = input("Enter your email address\n")
                regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
                if re.match(regex, email):
                    print("-----------------------------------")
                    password = input("Enter your password\n")
                    pm.register(email, password)
                    print("Please login")
                    trying_to_login = True
                    while trying_to_login:
                        email = input("Enter your email to login\n")
                        regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
                        if re.match(regex, email):
                            password = input("Enter your password\n")
                            pm.login(email, password)
                            user = pm.logged_in_user
                            if user:
                                print(f"user logged in as {pm.logged_in_user.email}")
                                logged_in = True
                                trying_to_login = False
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
                                print("Incorrect details,try again")
                                
                        else:
                          print("x Incorrect email provided")



                    
                    
            correct = True

            
        else:
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            print("Please provide a valid option")
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

if __name__ == '__main__':
    main()
