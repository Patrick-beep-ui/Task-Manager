import tkinter as tk
from tkcalendar import DateEntry
from Task import Task
from datetime import datetime, timedelta

class CalendarView:
    def __init__(self, root, user_id, task_gui):
        self.root = root
        self.user_id = user_id
        self.task_gui = task_gui
        
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
        self.task_gui.update_task_list(tasks)

    def show_tasks_for_today(self):
        today = datetime.today().strftime("%#m/%#d/%y")
        tasks = Task(None, None, None, None, None).get_tasks_for_date(self.user_id, today)
        self.task_gui.update_task_list(tasks)

    def show_tasks_for_current_week(self):
        today = datetime.today()
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        
        start_formatted = start_of_week.strftime("%#m/%#d/%y")
        end_formatted = end_of_week.strftime("%#m/%#d/%#y")
        
        print("start_date:", start_formatted)
        print("end_date:", end_formatted)
        
        tasks = Task(None, None, None, None, None).get_tasks_for_week(self.user_id, start_formatted, end_formatted)
        self.task_gui.update_task_list(tasks)

    def show_tasks_for_current_month(self):
        today = datetime.today()
        start_of_month = today.replace(day=1)
        end_of_month = start_of_month.replace(day=28) + timedelta(days=4)
        end_of_month = end_of_month - timedelta(days=end_of_month.day)
        
        start_formatted = start_of_month.strftime("%#m/%#d/%y")
        end_formatted = end_of_month.strftime("%#m/%#d/%y")
        
        print("Month start_date:", start_formatted)
        print("Month end_date:", end_formatted)
        
        tasks = Task(None, None, None, None, None).get_tasks_for_period(self.user_id, start_formatted, end_formatted)
        self.task_gui.update_task_list(tasks)


if __name__ == "__main__":
    user_id = None 
    root = tk.Tk()
    app = CalendarView(root, user_id)
    root.mainloop()
