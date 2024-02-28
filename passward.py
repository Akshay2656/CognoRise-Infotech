import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length, allow_uppercase, allow_lowercase, allow_digits, allow_special_chars):
    characters = ''
    if allow_uppercase:
        characters += string.ascii_uppercase
    if allow_lowercase:
        characters += string.ascii_lowercase
    if allow_digits:
        characters += string.digits
    if allow_special_chars:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("No character types selected")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_button_clicked():
    try:
        length = int(length_entry.get())
        allow_uppercase = uppercase_var.get()
        allow_lowercase = lowercase_var.get()
        allow_digits = digits_var.get()
        allow_special_chars = special_chars_var.get()
        
        password = generate_password(length, allow_uppercase, allow_lowercase, allow_digits, allow_special_chars)
        
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError as e:
        messagebox.showerror("Error", e)

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2
    
    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

root = tk.Tk()
root.title("Password Generator")
root.configure(bg='#000000')  

title_font = ('Helvetica', 16, 'bold')
label_font = ('Helvetica', 12)
button_font = ('Helvetica', 12, 'bold')

window_width = 600
window_height = 500

center_window(root, window_width, window_height)

frame = tk.Frame(root, bg='#C0C0C0', bd=10, relief='ridge')
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

title_label = tk.Label(frame, text="Password Generator", font=title_font, bg='#590000', fg='white')
title_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

length_label = tk.Label(frame, text="Password Length:", font=label_font, bg='#934915',fg='white')
length_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
length_entry = tk.Entry(frame, font=label_font)
length_entry.grid(row=1, column=1, padx=5, pady=5)

uppercase_var = tk.BooleanVar()
uppercase_checkbutton = tk.Checkbutton(frame, text="Uppercase", variable=uppercase_var, font=label_font, bg='#C7F3F3')
uppercase_checkbutton.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

lowercase_var = tk.BooleanVar()
lowercase_checkbutton = tk.Checkbutton(frame, text="Lowercase", variable=lowercase_var, font=label_font, bg='#C7F3F3')
lowercase_checkbutton.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

digits_var = tk.BooleanVar()
digits_checkbutton = tk.Checkbutton(frame, text="Digits", variable=digits_var, font=label_font, bg='#C7F3F3')
digits_checkbutton.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
  
special_chars_var = tk.BooleanVar()
special_chars_checkbutton = tk.Checkbutton(frame, text="Special Characters", variable=special_chars_var, font=label_font, bg='#C7F3F3')
special_chars_checkbutton.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)

password_label = tk.Label(frame, text="Generated Password:", font=label_font, bg='red')
password_label.grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)
password_entry = tk.Entry(frame, width=30, font=label_font)
password_entry.grid(row=6, column=1, padx=5, pady=5)

generate_password_button = tk.Button(frame, text="Generate Password", command=generate_password_button_clicked, font=button_font, bg='#00B200', fg='white')
generate_password_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W+tk.E)

root.mainloop()
