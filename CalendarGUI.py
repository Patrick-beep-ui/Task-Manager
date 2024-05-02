import tkinter as tk
from tkcalendar import Calendar, DateEntry
from Task import Task
from datetime import datetime, timedelta
from tkinter import messagebox

class CalendarView:
    def __init__(self, root, user_id):
        self.root = root
        self.user_id = user_id
        
        self.cal_date = DateEntry(root, background='darkblue', foreground='white', borderwidth=2)
        self.cal_date.pack(padx=10, pady=10)
        
        self.button_show_tasks = tk.Button(root, text="Show Tasks", command=self.show_tasks_for_selected_date)
        self.button_show_tasks.pack(padx=5, pady=5)

        self.button_today = tk.Button(root, text="Today", command=self.show_tasks_for_today)
        self.button_today.pack(padx=5, pady=5)

        self.button_week = tk.Button(root, text="This Week", command=self.show_tasks_for_current_week)
        self.button_week.pack(padx=5, pady=5)

        self.button_month = tk.Button(root, text="This Month", command=self.show_tasks_for_current_month)
        self.button_month.pack(padx=5, pady=5)
    
    def show_tasks_for_selected_date(self):
        selected_date = self.cal_date.get()
        formatted_date = datetime.strptime(selected_date, "%m/%d/%y").strftime("%#m/%#d/%y")
        
        tasks = Task(None, None, None, None, None).get_tasks_for_date(self.user_id, formatted_date)
        self.show_task_info(tasks, formatted_date)
        
    def show_tasks_for_today(self):
        today = datetime.today().strftime("%#m/%#d/%y")
        tasks = Task(None, None, None, None, None).get_tasks_for_date(self.user_id, today)
        self.show_task_info(tasks, "Today")

    def show_tasks_for_current_week(self):
        today = datetime.today()
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        
        start_formatted = start_of_week.strftime("%#m/%#d/%y")
        end_formatted = end_of_week.strftime("%#m/%#d/%y")
        
        print("start_date:", start_formatted)
        
        print("end_date:", end_formatted)
        
        tasks = Task(None, None, None, None, None).get_tasks_for_period(self.user_id, start_formatted, end_formatted)
        
        self.show_task_info(tasks, f"This Week ({start_formatted} - {end_formatted})")

    def show_tasks_for_current_month(self):
        today = datetime.today()
        start_of_month = today.replace(day=1)
        end_of_month = start_of_month.replace(day=28) + timedelta(days=4)
        end_of_month = end_of_month - timedelta(days=end_of_month.day)
        
        start_formatted = start_of_month.strftime("%#m/%#d/%y")
        end_formatted = end_of_month.strftime("%#m/%#d/%y")
        
        tasks = Task(None, None, None, None, None).get_tasks_for_period(self.user_id, start_formatted, end_formatted)
        self.show_task_info(tasks, f"This Month ({start_formatted} - {end_formatted})")
        
    def show_task_info(self, tasks, title):
        task_info_window = tk.Toplevel(self.root)
        task_info_window.title(f"Tasks for {title}")
        
        if tasks:
            task_details = "\n".join([f"- {task['Title']}" for task in tasks])
            label_tasks = tk.Label(task_info_window, text=f"Tasks for {title}:\n{task_details}")
            label_tasks.pack(padx=10, pady=10)
        else:
            label_no_tasks = tk.Label(task_info_window, text="No tasks scheduled for this period.")
            label_no_tasks.pack(padx=10, pady=10)

if __name__ == "__main__":
    user_id = None 
    root = tk.Tk()
    app = CalendarView(root, user_id)
    root.mainloop()
