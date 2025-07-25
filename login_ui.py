import tkinter as tk
from tkinter import messagebox
import login_dal

def login():
    username = entry_username.get()
    password = entry_password.get()
    
    if login_dal.validate_user(username, password):
        messagebox.showinfo("Login", "Login successful!")
    else:
        messagebox.showerror("Login", "Invalid username or password.")

root = tk.Tk()
root.title("Login UI")
root.geometry("300x150")

tk.Label(root, text="Username:").pack(pady=(10, 0))
entry_username = tk.Entry(root)
entry_username.pack()

tk.Label(root, text="Password:").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

tk.Button(root, text="Login", command=login).pack(pady=10)

root.mainloop()
