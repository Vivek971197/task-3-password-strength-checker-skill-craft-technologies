import re
import tkinter as tk
from tkinter import messagebox

def check_strength(pwd):
    score = 0
    tips = []

    if len(pwd) >= 8:
        score += 1
    else:
        tips.append("Make it at least 8 characters long.")

    if re.search(r"[A-Z]", pwd):
        score += 1
    else:
        tips.append("Add some uppercase letters.")

    if re.search(r"[a-z]", pwd):
        score += 1
    else:
        tips.append("Add some lowercase letters.")

    if re.search(r"\d", pwd):
        score += 1
    else:
        tips.append("Include some numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", pwd):
        score += 1
    else:
        tips.append("Throw in some special characters like !@#$%.")

    if score == 5:
        strength = "Very Strong"
    elif score >= 3:
        strength = "Okay, but could be stronger"
    else:
        strength = "Weak"

    return strength, tips

def on_button_click():
    password = pwd_entry.get()
    if not password:
        messagebox.showwarning("Oops!", "Please enter a password first.")
        return

    strength, advice = check_strength(password)
    display_text = f"Your password is: {strength}\n"
    if advice:
        display_text += "Tips to improve:\n" + "\n".join(f"• {tip}" for tip in advice)
    else:
        display_text += "Nice! Your password looks solid."

    result_label.config(text=display_text)

def toggle_visibility():
    if show_var.get():
        pwd_entry.config(show="")
    else:
        pwd_entry.config(show="*")

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")
root.resizable(False, False)

tk.Label(root, text="Enter your password:", font=("Helvetica", 12)).pack(pady=12)

pwd_entry = tk.Entry(root, font=("Helvetica", 12), width=28, show="*")
pwd_entry.pack(pady=6)

show_var = tk.IntVar()
show_checkbox = tk.Checkbutton(root, text="Show Password", variable=show_var, command=toggle_visibility)
show_checkbox.pack()

check_btn = tk.Button(root, text="Check Password", font=("Helvetica", 12), command=on_button_click)
check_btn.pack(pady=12)

result_label = tk.Label(root, text="", font=("Helvetica", 11), fg="darkgreen", justify="left")
result_label.pack(pady=10)

root.mainloop()

