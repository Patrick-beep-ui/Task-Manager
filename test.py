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
