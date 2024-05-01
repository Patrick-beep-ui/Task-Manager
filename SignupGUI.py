import tkinter as tk
from tkinter import messagebox
from User import User

class SignupGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Signup")
        self.root.minsize(300, 200)
        
        self.root.configure(bg="#282a36")
        
        self.label_first_name = tk.Label(root, text="First Name:")
        self.label_first_name.grid(row=0, column=0, padx=5, pady=5)
        self.entry_first_name = tk.Entry(root)
        self.entry_first_name.grid(row=0, column=1, padx=5, pady=5)
        
        self.label_last_name = tk.Label(root, text="Last Name:")
        self.label_last_name.grid(row=1, column=0, padx=5, pady=5)
        self.entry_last_name = tk.Entry(root)
        self.entry_last_name.grid(row=1, column=1, padx=5, pady=5)
        
        self.label_username = tk.Label(root, text="Username:")
        self.label_username.grid(row=2, column=0, padx=5, pady=5)
        self.entry_username = tk.Entry(root)
        self.entry_username.grid(row=2, column=1, padx=5, pady=5)
        
        self.label_password = tk.Label(root, text="Password:")
        self.label_password.grid(row=3, column=0, padx=5, pady=5)
        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.grid(row=3, column=1, padx=5, pady=5)
        
        self.button_signup = tk.Button(root, text="Signup", command=self.signup)
        self.button_signup.grid(row=4, columnspan=2, padx=5, pady=5)
        
    def signup(self):
        from MainGUI import MainMenuGUI
        first_name = self.entry_first_name.get()
        last_name = self.entry_last_name.get()
        username = self.entry_username.get()
        password = self.entry_password.get()
        
        if first_name and last_name and username and password:
            user = User(first_name, last_name, username, password)
            user.create_user()
            messagebox.showinfo("Signup", "Signup Successful")
            # Redirect to the main GUI so that the user can test the login
            self.root.destroy()
            root = tk.Tk()
            app = MainMenuGUI(root)
            root.mainloop()
        else:
            messagebox.showwarning("Error", "Please fill in all the fields.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SignupGUI(root)
    root.mainloop()
