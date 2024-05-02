from Task import Task
from datetime import datetime

current_date = datetime.now().strftime("%d/%m/%Y")

user_id = 2
attribute = "State"
value = "Completed"

task = Task("Complete Software Project", "Completed", "01/05/2024", "Low", 2)
comments = task.show_comments(2, 1)
#print(comments)

#task.add_comment(2, 2, "This Project is absurd")

task.delete_comment(2,1, "Hola")

current_date = datetime.now().strftime("%#m/%#d/%y")
print(current_date)

# Call the filter_task method to filter tasks
task_manager = Task(None, None, None, None, None)
filtered_tasks = task_manager.get_tasks_for_date(user_id, current_date)

# Print the filtered tasks
for task in filtered_tasks:
    print(task)
    
task = Task("Complete Software Project", "Completed", "01/05/2024", "Low", 2, ["Great work!", "Well done!"])


#u2 = User("Cynthia", "Nicolas", "icypinks", "12345678")
#u2.create_file()

#print(u)
#print(u2)
""" 
from User import User
from Task import Task
from Login import Login
import json

username = input("Enter username: ")
password = input("Enter password: ")
login = Login(username, password)
if login.authenticate():
    print("Login successful")
else:
    print("Login Failed. Username or Password incorrect")
    

user_id = 1 
task_id = 2

    
task = Task("Test", "Test", "30/04/2024", "High", 1)
task.create_task()

task_instance = Task("Title", "State", "Date", "Priority", user_id)
show = task_instance.show_tasks(user_id)
print(show)


new_task_data = {
    "Title": "Python Project",
    "State": "Completed",
    "Date": "02/05/2024",
    "Priority": "High"
}
"""

# Assuming you have already authenticated the user
# Instantiate a Task object
#task_instance = Task("Title", "State", "Date", "Priority", user_id)

# Call the edit_task method on the task_instance
"""
if task_instance.edit_task(user_id, task_id, new_task_data):
    print("Task edited successfully")
else:
    print("Task editing failed")
"""



# Create a new task instance (not sure if you need this here)
#newTask = Task()
