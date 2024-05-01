import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, simpledialog
from tkcalendar import DateEntry  # Import the DateEntry widget
from Task import Task

class TaskGUI:
    id = None
    def __init__(self, root, user_id):
        self.root = root
        self.root.title("Task Manager")
        self.user_id = user_id
        
        self.root.configure(bg="#282a36")
        
        # Creating a frame to hold the task list
        self.task_frame = ttk.Frame(root)
        self.task_frame.pack(padx=10, pady=10)

        # Creating a treeview widget to display tasks
        self.tree = ttk.Treeview(self.task_frame, columns=("ID", "Title", "State", "Date", "Priority"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Title", text="Title")
        self.tree.heading("State", text="State")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Priority", text="Priority")
        self.tree.pack(fill="both", expand=True)

        # Buttons for CRUD functionality
        self.button_add = tk.Button(root, text="Add Task", command=self.open_add_task_window, bg="#007bff", fg="white")
        self.button_add.pack(side="left", padx=5, pady=5)
        
        self.button_edit = tk.Button(root, text="Edit Task", command=self.edit_task, bg="#ffc107", fg="black")
        self.button_edit.pack(side="left", padx=5, pady=5)
        
        self.button_delete = tk.Button(root, text="Delete Task", command=self.delete_task, bg="#dc3545", fg="white")
        self.button_delete.pack(side="left", padx=5, pady=5)

        self.populate_tasks()

    def populate_tasks(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        tasks = Task(None, None, None, None, None).show_tasks(self.user_id)

        for task in tasks:
            self.tree.insert("", "end", values=(task["ID"], task["Title"], task["State"], task["Date"], task["Priority"]))
    
    def open_add_task_window(self):
        # Create a new window for adding a task
        add_task_window = tk.Toplevel(self.root)
        add_task_window.title("Add Task")

        # Create labels and entry fields for task attributes
        label_title = tk.Label(add_task_window, text="Title:")
        label_title.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        entry_title = tk.Entry(add_task_window)
        entry_title.grid(row=0, column=1, padx=5, pady=5, sticky="we")

        label_state = tk.Label(add_task_window, text="State:")
        label_state.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        entry_state = ttk.Combobox(add_task_window, values=["Pending", "In Progress", "Completed"], state="readonly")
        entry_state.grid(row=1, column=1, padx=5, pady=5, sticky="we")

        label_date = tk.Label(add_task_window, text="Date:")
        label_date.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        cal_date = DateEntry(add_task_window, background='darkblue', foreground='white', borderwidth=2)
        cal_date.grid(row=2, column=1, padx=5, pady=5, sticky="we")

        label_priority = tk.Label(add_task_window, text="Priority:")
        label_priority.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        entry_priority = ttk.Combobox(add_task_window, values=["Normal", "Medium", "High"], state="readonly")
        entry_priority.grid(row=3, column=1, padx=5, pady=5, sticky="we")

        # Create Add and Cancel buttons
        button_add = tk.Button(add_task_window, text="Add", command=lambda: self.add_task(add_task_window, entry_title.get(), entry_state.get(), cal_date.get(), entry_priority.get()), bg="#007bff", fg="white")
        button_add.grid(row=4, column=0, columnspan=2, pady=10)

        button_cancel = tk.Button(add_task_window, text="Cancel", command=add_task_window.destroy, bg="#dc3545", fg="white")
        button_cancel.grid(row=5, column=0, columnspan=2)

    def add_task(self, window, title, state, date, priority):
        if title and state and date and priority:
            new_task = Task(title, state, date, priority, self.user_id)  
            new_task.create_task()
            window.destroy()
            self.populate_tasks()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")
    

    def edit_task(self):
        selected_item = self.tree.selection()
        if selected_item:
            task_id = self.tree.item(selected_item)["values"][0]
            task_details = self.tree.item(selected_item)["values"][1:]

            # Create a new window for editing the task
            edit_task_window = tk.Toplevel(self.root)
            edit_task_window.title("Edit Task")

            
            label_title = tk.Label(edit_task_window, text="Title:")
            label_title.grid(row=0, column=0, padx=5, pady=5, sticky="w")
            entry_title = tk.Entry(edit_task_window)
            entry_title.grid(row=0, column=1, padx=5, pady=5, sticky="we")
            entry_title.insert(0, task_details[0])  

            label_state = tk.Label(edit_task_window, text="State:")
            label_state.grid(row=1, column=0, padx=5, pady=5, sticky="w")
            entry_state = ttk.Combobox(edit_task_window, values=["Pending", "In Progress", "Completed"], state="readonly")
            entry_state.grid(row=1, column=1, padx=5, pady=5, sticky="we")
            entry_state.insert(0, task_details[1])  

            label_date = tk.Label(edit_task_window, text="Date:")
            label_date.grid(row=2, column=0, padx=5, pady=5, sticky="w")
            cal_date = DateEntry(edit_task_window, background='darkblue', foreground='white', borderwidth=2)
            cal_date.grid(row=2, column=1, padx=5, pady=5, sticky="we")
            cal_date.set_date(task_details[2])  

            label_priority = tk.Label(edit_task_window, text="Priority:")
            label_priority.grid(row=3, column=0, padx=5, pady=5, sticky="w")
            entry_priority = ttk.Combobox(edit_task_window, values=["Normal", "Medium", "High"], state="readonly")
            entry_priority.grid(row=3, column=1, padx=5, pady=5, sticky="we")
            entry_priority.insert(0, task_details[3])  

            # Create Update and Cancel buttons
            button_update = tk.Button(edit_task_window, text="Update", command=lambda: self.update_task(edit_task_window, task_id, entry_title.get(), entry_state.get(), cal_date.get(), entry_priority.get()), bg="#007bff", fg="white")
            button_update.grid(row=4, column=0, columnspan=2, pady=10)

            button_cancel = tk.Button(edit_task_window, text="Cancel", command=edit_task_window.destroy, bg="#dc3545", fg="white")
            button_cancel.grid(row=5, column=0, columnspan=2)
        else:
            messagebox.showinfo("Edit Task", "Please select a task to edit.")
        
    
    def update_task(self, window, task_id, title, state, date, priority):
        if title and state and date and priority:
            new_task_data = {
                "Title": title,
                "State": state,
                "Date": date,
                "Priority": priority
            }
            task = Task(None, None, None, None, None)
            task.edit_task(self.user_id, task_id, new_task_data)
            window.destroy()
            self.populate_tasks()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def delete_task(self):
        # Get the selected item from the treeview
        selected_item = self.tree.selection()
        if selected_item:
            # Get the task ID from the selected item
            task_id = self.tree.item(selected_item)["values"][0]
            task = Task(None, None, None, None, None)
            task.delete_task(self.user_id, task_id)
            self.populate_tasks()
        else:
            messagebox.showinfo("Delete Task", "Please select a task to delete.")

    def select_date(self, initial_date=None):
        # Create a new window for selecting the date
        self.date_window = tk.Toplevel(self.root)
        self.date_window.title("Select Date")
        self.cal_date = DateEntry(self.date_window, background='darkblue', foreground='white', borderwidth=2)
        self.cal_date.pack(padx=10, pady=10)

        # Set initial date if provided
        if initial_date:
            self.cal_date.set_date(initial_date)

        # button to confirm the date selection
        button_confirm = tk.Button(self.date_window, text="Confirm", command=self.confirm_date, bg="#007bff", fg="white")
        button_confirm.pack(pady=5)

    def confirm_date(self):
        # Store the selected date in the instance variable
        self.selected_date = self.cal_date.get()
        # Destroy the date selection window
        self.date_window.destroy()

if __name__ == "__main__":
    user_id = None 

    root = tk.Tk()
    app = TaskGUI(root, user_id)
    root.mainloop()
