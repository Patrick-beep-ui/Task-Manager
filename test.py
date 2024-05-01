from Task import Task

user_id = 2
attribute = "State"
value = "Completed"

# Call the filter_task method to filter tasks
task_manager = Task(None, None, None, None, None)
filtered_tasks = task_manager.get_tasks_for_date(user_id, '5/1/24')

# Print the filtered tasks
for task in filtered_tasks:
    print(task)