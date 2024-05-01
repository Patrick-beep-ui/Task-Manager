from User import User
from Task import Task
from Login import Login
import json

#u = User("Patrick", "Solis", "Psolis18", "patrick18")
#u.create_file()

#u2 = User("Cynthia", "Nicolas", "icypinks", "12345678")
#u2.create_file()

#print(u)
#print(u2)

from User import User
from Task import Task
from Login import Login
import json

username = input("Enter username: ")
password = input("Enter password: ")
login = Login(username, password)
if login.authenticate():
    print("Login successful")
    

user_id = 2 
task_id = 2

new_task_data = {
    "Title": "Python Project",
    "State": "Completed",
    "Date": "02/05/2024",
    "Priority": "High"
}

# Assuming you have already authenticated the user
# Instantiate a Task object
task_instance = Task("Title", "State", "Date", "Priority", user_id)

# Call the edit_task method on the task_instance
if task_instance.edit_task(user_id, task_id, new_task_data):
    print("Task edited successfully")
else:
    print("Task editing failed")


# Create a new task instance (not sure if you need this here)
#newTask = Task()

    
#ask = Task("Deliver Software Assignments", "Pending", "30/04/2024", "High", 2)