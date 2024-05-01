import tkinter as tk
from tkinter import messagebox
from Login import Login
from TaskGUI import TaskGUI

class LoginGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.minsize(300, 200)
        
        self.root.configure(bg="#282a36")

        self.label_username = tk.Label(root, text="Username:", bg="#282a36", fg="#fff")
        self.label_username.pack(pady=5)
        self.entry_username = tk.Entry(root)
        self.entry_username.pack(pady=5)

        self.label_password = tk.Label(root, text="Password:", bg="#282a36", fg="#fff")
        self.label_password.pack(pady=5)
        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.pack(pady=5)

        self.button_login = tk.Button(root, text="Login", command=self.login)
        self.button_login.pack(pady=10)

    def login(self):
        from User import User
        username = self.entry_username.get()
        password = self.entry_password.get()
        
        if username and password:
            login = Login(username, password)
            if login.authenticate():
                user = User(None, None, None, None)  
                user_id = user.find_user_id_by_username(username)
                if user_id is not None:
                    # Create an instance of the Task GUI and pass the user ID
                    self.root.withdraw() 
                    task_root = tk.Toplevel()
                    task_app = TaskGUI(task_root, user_id)
                else:
                    messagebox.showerror("Error", "User ID not found.")
            else:
                messagebox.showerror("Error","Invalid username or password")
        else:
            messagebox.showwarning("Warning","Please enter username and password")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginGUI(root)
    root.mainloop()
