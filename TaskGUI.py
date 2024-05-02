import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, simpledialog
from tkcalendar import DateEntry  
from Task import Task
import matplotlib.pyplot as plt
from datetime import datetime

class TaskGUI:
    id = None
    def __init__(self, root, user_id):
        self.root = root
        self.root.title("Task Manager")
        self.user_id = user_id
        self.task_id = None
        
        self.root.configure(bg="#282a36")
        
        # Frame to hold the task list
        self.task_frame = ttk.Frame(root)
        self.task_frame.pack(padx=10, pady=10)

        # Treeview widget to display tasks
        self.tree = ttk.Treeview(self.task_frame, columns=("ID", "Title", "State", "Date", "Priority"), show="headings")
        self.tree.heading("ID", text="ID", command=lambda: self.sort_tasks("ID"))
        self.tree.heading("Title", text="Title", command=lambda: self.sort_tasks("Title"))
        self.tree.heading("State", text="State", command=lambda: self.sort_tasks("State"))
        self.tree.heading("Date", text="Date", command=lambda: self.sort_tasks("Date"))
        self.tree.heading("Priority", text="Priority", command=lambda: self.sort_tasks("Priority"))
        self.tree.pack(fill="both", expand=True)

        # Buttons for CRUD functionality
        self.button_add = tk.Button(root, text="Add Task", command=self.open_add_task_window, bg="#007bff", fg="white")
        self.button_add.pack(side="left", padx=5, pady=5)
        
        self.button_edit = tk.Button(root, text="Edit Task", command=self.edit_task, bg="#ffc107", fg="black")
        self.button_edit.pack(side="left", padx=5, pady=5)
        
        self.button_delete = tk.Button(root, text="Delete Task", command=self.delete_task, bg="#dc3545", fg="white")
        self.button_delete.pack(side="left", padx=5, pady=5)
        
        # Bar graph for task completion
        self.button_display_graph = tk.Button(root, text="Display Graph", command=self.display_graph_window, bg="#28a745", fg="white")
        self.button_display_graph.pack(side="left", padx=5, pady=5)

        #self.populate_tasks()
        self.populate_tasks_for_current_day()
        
        #Filters
        self.button_filter = tk.Button(root, text="Filter", command=self.open_filter_window, bg="#28a745", fg="white")
        self.button_filter.pack(side="left", padx=5, pady=5)
        self.button_filter_delete = tk.Button(root, text="Delete Filter", command=self.populate_tasks, bg="#dc3545", fg="white")
        self.button_filter_delete.pack(side="left", padx=5, pady=5)
        
        self.button_show_tasks = tk.Button(root, text="See all tasks", command=self.populate_tasks, bg="#bd9319", fg="white")
        self.button_show_tasks.pack(side="left", padx=5, pady=5)
        
        #Comments
        self.button_show_comments = tk.Button(root, text="Show Comments", command=self.open_comments_window, bg="#bd9319", fg="white")
        self.button_show_comments.pack(side="left", padx=5, pady=5)
        
        self.comment_listbox = tk.Listbox()

    def populate_tasks_for_current_day(self):
        self.clear_tasks()

        current_date = datetime.now().strftime("%#m/%#d/%y")

        # Get tasks for the current day
        tasks = Task(None, None, None, None, None).get_tasks_for_date(self.user_id, current_date)

        self.get_tasks_by_date(tasks)
    
    def clear_tasks(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
    
    def get_tasks_by_date(self, tasks):
        for task in tasks:
            self.tree.insert("", "end", values=(task["ID"], task["Title"], task["State"], task["Date"], task["Priority"]))

    def populate_tasks(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        tasks = Task(None, None, None, None, None).show_tasks(self.user_id)

        for task in tasks:
            self.tree.insert("", "end", values=(task["ID"], task["Title"], task["State"], task["Date"], task["Priority"]))

    
    def open_add_task_window(self):
        add_task_window = tk.Toplevel(self.root)
        add_task_window.title("Add Task")

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
            
    
    def sort_tasks(self, column):
        for item in self.tree.get_children():
            self.tree.delete(item)
        tasks = Task(None, None, None, None, None).show_tasks(self.user_id)
        tasks.sort(key=lambda x: x[column])

    
        for task in tasks:
            self.tree.insert("", "end", values=(task["ID"], task["Title"], task["State"], task["Date"], task["Priority"]))


###################### Date ###################

    def select_date(self, initial_date=None):
        # Create a new window for selecting the date
        self.date_window = tk.Toplevel(self.root)
        self.date_window.title("Select Date")
        self.cal_date = DateEntry(self.date_window, background='darkblue', foreground='white', borderwidth=2)
        self.cal_date.pack(padx=10, pady=10)
        
        if initial_date:
            self.cal_date.set_date(initial_date)

        # button to confirm the date selection
        button_confirm = tk.Button(self.date_window, text="Confirm", command=self.confirm_date, bg="#007bff", fg="white")
        button_confirm.pack(pady=5)

    def confirm_date(self):
        self.selected_date = self.cal_date.get()
        self.date_window.destroy()
    
    ################ Graph ################
    def display_graph_window(self):
        graph_window = tk.Toplevel(self.root)
        graph_window.title("Task Completion Status")

        # Plotting the bar graph
        tasks = Task(None, None, None, None, None).show_tasks(self.user_id)
        completion_counts = {"Pending": 0, "In Progress": 0, "Completed": 0}
        for task in tasks:
            completion_counts[task["State"]] += 1
        print(completion_counts)


        plt.figure(figsize=(6, 4))
        plt.bar(completion_counts.keys(), completion_counts.values(), color=["red", "orange", "green"])
        plt.xlabel("Task State")
        plt.ylabel("Number of Tasks")
        plt.title("Task Completion Status")
        plt.tight_layout()
        plt.show()
        
    ############## Filters ##############
    def open_filter_window(self):
        # Create a new window for filtering tasks
        filter_window = tk.Toplevel(self.root)
        filter_window.title("Filter Tasks")

        label_attribute = tk.Label(filter_window, text="Attribute:")
        label_attribute.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        attributes = ["Title", "State", "Date", "Priority"]
        combobox_attribute = ttk.Combobox(filter_window, values=attributes, state="readonly")
        combobox_attribute.grid(row=0, column=1, padx=5, pady=5, sticky="we")

        label_value = tk.Label(filter_window, text="Value:")
        label_value.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        entry_value = tk.Entry(filter_window)
        entry_value.grid(row=1, column=1, padx=5, pady=5, sticky="we")

        button_filter = tk.Button(filter_window, text="Filter", command=lambda: self.apply_filter(filter_window, combobox_attribute.get(), entry_value.get()), bg="#007bff", fg="white")
        button_filter.grid(row=2, column=0, columnspan=2, pady=10)

        button_cancel = tk.Button(filter_window, text="Cancel", command=filter_window.destroy, bg="#dc3545", fg="white")
        button_cancel.grid(row=3, column=0, columnspan=2)
        
    def apply_filter(self, window, attribute, value):
        filtered_tasks = Task(None, None, None, None, None).filter_task(self.user_id, attribute, value)
        window.destroy()
        self.update_task_list(filtered_tasks)


    def update_task_list(self, tasks):
        # Clear the treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insert the filtered tasks into the treeview
        for task in tasks:
            self.tree.insert("", "end", values=(task["id"], task["Title"], task["State"], task["Date"], task["Priority"]))
            
    ############## Comments ###############
    def open_comments_window(self):
            selected_item = self.tree.selection()
            if selected_item:
                self.task_id = self.tree.item(selected_item)["values"][0]
                task = Task(None, None, None, None, None)
                comments = task.show_comments(self.user_id, self.task_id)
                if comments:
                    comments_window = tk.Toplevel(self.root)
                    comments_window.title("Task Comments")

                    label_comments = tk.Label(comments_window, text="Comments:")
                    label_comments.grid(row=0, column=0, padx=5, pady=5, sticky="w")

                    self.comment_listbox = tk.Listbox(comments_window, width=50)
                    self.comment_listbox.grid(row=1, column=0, padx=5, pady=5)
                    self.comment_listbox.bind("<<ListboxSelect>>", self.on_comment_select)

                    for comment in comments:
                        self.comment_listbox.insert(tk.END, comment)
                    
                    #add comment
                    self.button_add_comment = tk.Button(comments_window, text="Add Comment", command=self.open_add_comment_window)
                    self.button_add_comment.grid(row=2, column=0, padx=5, pady=5)
                    
                    self.button_delete_comment = tk.Button(comments_window, text="Delete Comment", command=self.delete_task_comment)
                    self.button_delete_comment.grid(row=2, column=1, padx=5, pady=5)
                    
                else:
                    messagebox.showinfo("Task Comments", "No comments available for this task.")
            else:
                messagebox.showinfo("Task Comments", "Please select a task to view comments.")
    
    def open_add_comment_window(self):
        add_comment_window = tk.Toplevel(self.root)
        add_comment_window.title("Add Comment")

        label_comment = tk.Label(add_comment_window, text="Comment:")
        label_comment.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.entry_comment = tk.Entry(add_comment_window, width=50)
        self.entry_comment.grid(row=0, column=1, padx=5, pady=5)

        button_confirm = tk.Button(add_comment_window, text="Confirm", command=self.add_comment_to_task, bg="#007bff", fg="white")
        button_confirm.grid(row=1, column=0, padx=5, pady=5)

        button_cancel = tk.Button(add_comment_window, text="Cancel", command=add_comment_window.destroy, bg="#dc3545", fg="white")
        button_cancel.grid(row=1, column=1, padx=5, pady=5)
        
    def on_comment_select(self, event):
        selected_index = self.comment_listbox.curselection()
        if selected_index:
            selected_comment = self.comment_listbox.get(selected_index)
            self.selected_comment = selected_comment 
        else:
            self.selected_comment = None

    def add_comment_to_task(self):
        comment_text = self.entry_comment.get()
        if comment_text:
            task = Task(None, None, None, None, None)
            task.add_comment(self.user_id, self.task_id, comment_text)
            self.comment_listbox.insert(tk.END, comment_text)
        else:
            messagebox.showinfo("Add Comment", "Please enter a comment.")

    def delete_task_comment(self):
        if self.selected_comment:
            task = Task(None, None, None, None, None)
            task.delete_comment(self.user_id, self.task_id, self.selected_comment)
            self.comment_listbox.delete(self.comment_listbox.curselection())
            messagebox.showwarning("Delete Comment", "Comment deleted successfully")
        else:
            messagebox.showinfo("Add Comment", "Please enter a comment.")


if __name__ == "__main__":
    user_id = None 

    root = tk.Tk()
    app = TaskGUI(root, user_id)
    root.mainloop()
