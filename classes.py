
import re
import csv
import hashlib
from typing import List


# Password Class
# Password class is used to create password objects with attributes (title, url, username, password)
class Password:
    # Init method is initialzied when the object is created
    def __init__(self, title, url, username, password):
        self.title = title
        self.url = url
        self.username = username
        self.password = password

# User Class
# User Class creates user object, saves userdata in userdata.csv, and creates Password objects to save user passwords data in passwords.csv
class User:
    # Init method takes defauls file name for storing passwords
    def __init__(self, email, password, file_name="passwords.csv"):
        self.email = email
        self.password = password
        self.file_name = file_name
        self.passwords: List[Password] = []

    # Create password method is used to store user passwords in the passwords.csv file, it returns successful message when password is saved, and also shows error message if the same title is used in one of the previously saved passwords by the user
    def create_password(self, title, url, username, password):
        user_passwords = []
        with open(self.file_name, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] == self.email:
                    user_passwords.append(row[1]) 
           
        if len(user_passwords) > 0:
         
            for pass_title in user_passwords:
           
           
                if pass_title == title:
                    print("=========================================")
                    print("Password already exists for this title, please choose a different title")
                    print("=========================================")
                    break
                
                else:
          
                    
                    with open(self.file_name, 'a') as file:
                        writer = csv.writer(file)
                        writer.writerow([self.email, title, url, username, password])
                        print("=========================================")
                        print(f"Password saved successfully for {title}.")
                        print("=========================================")
                        return True
    
        else: 
         
            with open(self.file_name, 'a') as file:
              writer = csv.writer(file)
              writer.writerow([self.email, title, url, username, password])
              print("=========================================")
              print(f"Password saved successfully for {title}.")
              print("=========================================")
              return True
    

           
    # This method is used to get all user specific passwords from the passwords.csv file
    def get_all_passwords(self):
        user_passwords = []
        with open(self.file_name, 'r',newline='') as file:
            reader = csv.reader(file)
            
      
            for row in reader:
                if row and row[0] == self.email:
                    user_passwords.append(row)
            
          
            if len(user_passwords) == 0:
                print("You have no passwords saved, try adding one.")
                return True
            print("Here are your passwords\n")
  
            for index, value in enumerate(user_passwords):
                print('--------------------------------')
                print(f"{index+1}: title: {value[1]}, url: {value[2]}, username: {value[3]}, password: {value[4]}")
                print('--------------------------------')
           

    # This method is used to delete one password from the list of logged in user passwords by matching title. Proper errors are setup in this method to guide the user.
    def delete_password(self, title):
        user_paswords = []
        removed = None
        new_list = []
        
        
        with open(self.file_name, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] == self.email:
                    user_paswords.append(row)

        if len(user_paswords) == 0:
            print('--------------------------------')
            print("You do not have any passwords saved")
            print('--------------------------------')
        else:
            for row in user_paswords:
                if row[1] == title:
                    removed = row
                    print('--------------------------------')
                    print(f"Password for {removed[1]} removed successfully\n")
                    print('--------------------------------')
                else:
                    new_list.append(row)
                   
            
        with open(self.file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(new_list)



# Password Manager Class
# PasswordManager Class is used to register and login the users, is also manages user authentication state using logged_in_user attribute
class PasswordManager:
    def __init__(self, file_name="userdata.csv"):
        self.logged_in_user: User | None = None
        self.file_name = file_name
    # register method is used to register user using its username and password
    def register(self, email, password):
        regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
        if re.match(regex, email):
            with open(self.file_name, 'r') as file:
                reader = csv.reader(file)
                user_found = False
                for row in reader:
                    if row[0] == email:
                        print("User already exists. Try loggin in.\n")
                        user_found = True
                        break
                if not user_found:
                    hash = hashlib.sha256(str(password).encode()).hexdigest()
                    with open(self.file_name, 'a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([email, hash])
                        print("Signed up successfully")
        else:
            print("Invalid email address provided")
   
    # login method logins the user with proper errors, and sets the log in state on success
    def login(self, email, password):
        regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
        hash = hashlib.sha256(str(password).encode()).hexdigest()
        if re.match(regex, email):
            hash = hashlib.sha256(str(password).encode()).hexdigest()
            with open(self.file_name, 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == email and row[1] == hash:
                        self.logged_in_user = User(email, password)
                        print("Logged in")
                        break
       
        else:
            print("Invalid email address provided")