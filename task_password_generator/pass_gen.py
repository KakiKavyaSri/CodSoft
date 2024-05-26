import tkinter as tk
from tkinter import messagebox, Frame
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Password length must be a number.")
        return
    
    complexity = complexity_var.get()

    if length <= 0:
        messagebox.showerror("Error", "Password length must be greater than 0.")
        return

    if complexity == "Low":
        characters = string.ascii_letters + string.digits
    elif complexity == "Medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "High":
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.config(state=tk.NORMAL)
    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)
    password_entry.config(state='readonly')

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Set the background color of the main window
root.configure(bg='#dcc4a8')

# Make the main window resizable
root.geometry("1000x1000")
root.resizable(True, True)

# Create a frame with the same background color
page = Frame(root, bg='#dcc4a8')
page.pack(fill=tk.BOTH, expand=True)

# Create title label
title_label = tk.Label(page, text="PASSWORD GENERATOR", font=("Roboto", 40, 'bold'), fg="#873e23", bg='#dcc4a8')
title_label.grid(row=0, column=0, columnspan=3, pady=10)

# Create labels and entry widgets
length_label = tk.Label(page, text="Password Length:", font=("Helvetica", 30), bg='#dcc4a8')
length_label.grid(row=1, column=0, padx=10, pady=(120, 10), sticky='e')  # Adjusted pady

length_entry = tk.Entry(page, font=("Helvetica", 30))
length_entry.grid(row=1, column=1, padx=10, pady=(120, 10), sticky='w')

complexity_label = tk.Label(page, text="Password Complexity:", font=("Helvetica", 30), bg='#dcc4a8')
complexity_label.grid(row=2, column=0, padx=10, pady=(80,10), sticky='e')  # Adjusted pady

complexity_var = tk.StringVar(root)
complexity_var.set("Low")
complexity_menu = tk.OptionMenu(page, complexity_var, "Low", "Medium", "High")
complexity_menu.config(font=("Helvetica", 30))
complexity_menu.grid(row=2, column=1, padx=10, pady=(80, 10), sticky='w')  # Adjusted pady

generate_button = tk.Button(page, text="Generate Password", font=("Helvetica", 30), command=generate_password)
generate_button.grid(row=3, column=0, padx=10, pady=(80, 10), sticky='e')  # Adjusted pady

password_entry = tk.Entry(page, width=50, font=("Helvetica", 35))
password_entry.grid(row=3, column=1, padx=10, pady=(80, 10), sticky='w')  # Adjusted pady
password_entry.config(state='readonly')

root.mainloop()
