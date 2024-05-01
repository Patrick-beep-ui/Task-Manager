from Task import Task
from datetime import datetime

current_date = datetime.now().strftime("%d/%m/%Y")

user_id = 2
attribute = "State"
value = "Completed"

current_date = datetime.now().strftime("%#m/%#d/%y")
print(current_date)

# Call the filter_task method to filter tasks
task_manager = Task(None, None, None, None, None)
filtered_tasks = task_manager.get_tasks_for_date(user_id, current_date)

# Print the filtered tasks
for task in filtered_tasks:
    print(task)