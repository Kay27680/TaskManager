#Program By: Keamogetswe Mashao
#This program works with multiple text files simulateously
#The program will allow user to view, manage and add tasks by means of a menu
#Admin will be able to register users and have a seperate statisics menu at the end of the program

#Importing packages
import datetime
from datetime import date


# Opening the text files
t1 = open("tasks.txt", "r+")
ofile = t1.read()
t2 = open("user.txt" , "r+")
ofile_1 = t2.read()

# Declaring test varibale
complete = False
#parameters for logon credentials
user = {"admin" : "adm1n", "Tom" : "12345" }
 
 #while condition to login and verify password and username
while not complete:
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    if username == user and password == password:
        continue
    elif username not in user:
        print("This is not a valid username, input username again!")
        continue
    elif password != user[username]:
        print(f"Password is not valid for {username}. ")
        continue
    elif password == user[username]:
        print(f"Welcome {username} ")
        print(f"Thank you for logging on. ")
        complete = True
 
print ("Username and Password are valid you can proceed to the menu")

#Displayed menu option should the user have loggged on correctly
menu1 = """
Please select one of following options (r-e):
r) Register User
a) Add Task
va) View All Tasks
vm) View My Tasks
e) Exit
"""

option = str(input(menu1))
#option e ends the program automatically at any stage
while option != "e":
    if option == "r":
            #Only admin can register new users
            while username == "admin":
               #input credentials for new users
                username = input ("Please type in a new username for a new user: ")
                password = input ("Please type in a new password for a new user: ")
                confirm_password = input("Please confirm your password: ")
                #if the password and confiremed password are the same, credentials will be writen to user text
                if password == confirm_password:
                    result = username + confirm_password
                    t2.write("\n" + "the username for the new user is: "  + "," + username + ", " + "the password for the new user is: " + "," + confirm_password)
                    print ("Thank you for registering a new user")
                    t2.close()
                    #should the passwords not match the user won't be registered and the program will continue w
                    #having registering that user
                elif password != confirm_password:
                    password_wrong = print("passwords don't match")
                   
                   
            #condition statememnt should the user trying to regiser a new user not be admin
            if username != "admin":
                    print ("Only admin can register a new user")    
                
    #reopening files
    t1 = open("tasks.txt", "r+")
    ofile = t1.read()
    #option to add a new task
    if option == "a":
        #user inputs for parameters of new tasks
        username_1 = input ("Please enter the user you would like to assign the task to: ")
        task_name = input ("Please enter the title of the task: ")
        task_desc = input ("Please give a short description of what the task does: ")
        due_date = input ("Please give the due date for the task: ")
        completed = "No"
        #all info on new task will be written to the tasks file
        t1.write ("\n" + username_1 + ", " + task_name + ", " + task_desc + ", " + str(date.today()) + ", " + due_date + ", " + completed)
    
    #reopening filed    
    t1 = open("tasks.txt", "r+")
    ofile = t1.read()
    #option to view all task
    if option == "va":
        #program will print all current ongoing tasks to the terminal
        t1 = open("tasks.txt", "r+") 
        contents = t1.read()         
        t1.close()                   
        print(contents)
 
    #option to view a single users tasks
    if option == "vm":

        username1 = input ("Please enter the username to view tasks for user: ")
        #program will search for the username in text files and print out their allocated tasks
        search = open("tasks.txt")
        for line in search:
            if username1 in line:
                print (line) 

    option = str(input(menu1))

#new parameters for statistics menu
complete = False
user1 = {"admin" : "adm1n"}
 #only admin and no other user can access this menu
while not complete:
    print("Please enter login with admin credentials")
    username_stats = input("Please enter your username: ")
    password_stats = input("Please enter your password: ")
    if username_stats == user1 and password_stats == user1:
        continue
    elif username_stats not in user:
        print("This is not a valid username, input username again!")
        continue
    elif password_stats != user[username_stats]:
        print(f"Password is not valid for {username_stats}. ")
        continue
    elif password_stats == user[username_stats]:
        print(f"Welcome {username_stats} ")
        print(f"Thank you for logging on. ")
        complete = True
#if admin credentails are correct the admin menu will be display along with the statistics
print ("Username and Password are valid you can proceed to the menu to view the statistcs")
menu2 = """
Please select one of following options (r-s):
r) Register User
a) Add Task
va) View All Tasks
vm) View My Tasks
s) Statistics of tasks and users
e) Exit
"""

option = str(input(menu2))
#reopening files
t1 = open("tasks.txt", "r+")
ofile = t1.read()
t2 = open("user.txt" , "r+")
ofile_1 = t2.read()

#should admin want to view the statistics of the task
if option == "s":
    #info will be collected from the two text files with all the statsitics
    filenames = ['user.txt', 'tasks.txt'] 
    with open('Statistics.txt', 'r+') as outfile: 
   
        for string in filenames: 
  
        # Open each file in read mode 
         with open(string) as infile: 
            outfile.write(infile.read()) 
            #The statistics of the tasks will be writeen to the statistics text file in an easy to read manner
            outfile.write("\n") 
            print("Please view statistics in the statistics text.")