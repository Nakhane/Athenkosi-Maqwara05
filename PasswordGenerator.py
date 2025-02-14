import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip
import re

# Password Generator Function
def generate_password():
    length = int(length_var.get())
    if length < 6:
        messagebox.showwarning("Weak Password", "Choose a length of at least 6 for security.")
        return
    
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = "".join(random.choice(characters) for _ in range(length))
    
    password_var.set(password)
    strength_label.config(text=f"Password Strength is: {password_strength(password)}")

# Password Strength Checker
def password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*()]", password):
        score += 1
    return ["Weak", "Medium", "Strong", "Very Strong"][min(score, 3)]

# Enables the ability to copy to clipboard
def copy_to_clipboard():
    pyperclip.copy(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI Setup
root = tk.Tk()
root.title("LockIt")
root.geometry("400x300")
root.config(bg="#2C3E50")

# Length Label & Input
tk.Label(root, text="Password Length:", fg="white", bg="#2C3E50", font=("Arial", 12)).pack(pady=5)
length_var = tk.StringVar(value="12")
length_entry = tk.Entry(root, textvariable=length_var, width=5, font=("Arial", 12))
length_entry.pack()

# Generate Button
tk.Button(root, text="Get Password", command=generate_password, font=("Arial", 12), bg="#3498DB", fg="white").pack(pady=10)

# Password Display
password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, font=("Arial", 14), width=24, state="readonly")
password_entry.pack()

# Strength Label
strength_label = tk.Label(root, text="Password Strength is: ", fg="white", bg="#2C3E50", font=("Arial", 12))
strength_label.pack(pady=5)

# Copy Button
tk.Button(root, text="Copy Password", command=copy_to_clipboard, font=("Arial", 12), bg="#E74C3C", fg="white").pack(pady=10)

# Run the GUI
root.mainloop()
