import tkinter as tk
from LoginGUI import LoginGUI
from SignupGUI import SignupGUI

class MainMenuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Menu")
        self.root.minsize(300, 200)
        
        self.root.configure(bg="#282a36")

        self.label = tk.Label(root, text="Welcome to Task Manager", bg="#282a36", fg="#fff")
        self.label.pack(pady=10)

        self.button_signup = tk.Button(root, text="Signup", width=20, height=2, bg="#282a36", fg="#fff", command=self.open_signup)
        self.button_signup.pack(pady=5)

        self.button_login = tk.Button(root, text="Login", width=20, height=2, bg="#282a36", fg="#fff",command=self.open_login)
        self.button_login.pack(pady=5)

    def open_signup(self):
        self.root.destroy()
        root = tk.Tk()
        app = SignupGUI(root)
        root.mainloop()

    def open_login(self):
        self.root.destroy()  
        root = tk.Tk()
        app = LoginGUI(root)
        root.mainloop()


# Solution found to maintain the correct flow of GUIs
if __name__ == "__main__":
    root = tk.Tk()
    app = MainMenuGUI(root)
    root.mainloop()
