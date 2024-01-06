import tkinter as tk
import sqlite3
import pyperclip
import os
import string
import secrets

# Establish the database connection
conn = sqlite3.connect('passappbase.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS passappbase (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                login TEXT,
                password TEXT,
                application TEXT
                )''')
conn.commit()

# Function to execute SQL queries
def execute_query(query, *args):
    c.execute(query, args)
    conn.commit()

# Function to add password to the database
def add_password():
    execute_query('INSERT INTO passappbase (login, password, application) VALUES (?, ?, ?)',
                  entry_login.get(), entry_password.get(), entry_app.get())
    label_index.config(text=f"New password added. Index: {c.lastrowid}")

def generate_password():
    symbols = "0123456789!@#$%^&*()_+:|>?<\{\}"
    alphabet = string.ascii_letters + string.digits + symbols
    
    password = ''.join(secrets.choice(alphabet) for i in range(16))
    
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)
    
    pyperclip.copy(password)
    label_index.config(text="Password generated and copied", fg="blue")

# Function to retrieve password from the database
def retrieve_password():
    index_or_app = entry_fetch.get()
    c.execute('''SELECT login, password FROM passappbase WHERE id = ? OR login = ? OR application = ?''',
              (index_or_app, index_or_app, index_or_app))
    result = c.fetchone()
    if result:
        label_retrieved_password.config(text=f"Login: {result[0]}, Password: {result[1]}", fg="green")
        pyperclip.copy(result[1])  # Copying password to clipboard
    else:
        label_retrieved_password.config(text="Not found", fg="red")

# Function to copy login to clipboard
def copy_login():
    result_text = label_retrieved_password.cget("text")
    login = result_text.split("Login: ")[1].split(", Password: ")[0]
    pyperclip.copy(login)
    label_index.config(text="Login copied", fg="blue")

# Function to copy password to clipboard
def copy_password():
    result_text = label_retrieved_password.cget("text")
    password = result_text.split(", Password: ")[1]
    pyperclip.copy(password)
    label_index.config(text="Password copied", fg="blue")

# Function to clear the entire database
def clear_database():
    execute_query('''DELETE FROM passappbase''')
    execute_query('''DELETE FROM SQLITE_SEQUENCE WHERE name='passappbase' ''')
    label_index.config(text="Database cleared")
    entry_password.delete(0, tk.END)
    entry_app.delete(0, tk.END)
    entry_fetch.delete(0, tk.END)
    label_retrieved_password.config(text="")

# GUI setup
root = tk.Tk()
root.title("PaSaver")
root.geometry("800x800")
root.resizable(False, False)

canvas = tk.Canvas(root, width=450, height=100)
canvas.grid(row=0, column=0, columnspan=3)

# Load and display the image on the canvas
image_path = "PaSaver_blank.png"
image = tk.PhotoImage(file=image_path)
canvas.create_image(200, 50, anchor=tk.CENTER, image=image)

# UI components
label_login = tk.Label(root, text="Login / Email:", font=("Arial", 13))
entry_login = tk.Entry(root, font=("Arial", 13))
label_password = tk.Label(root, text="Password:", font=("Arial", 13))
entry_password = tk.Entry(root, font=("Arial", 13))
label_app = tk.Label(root, text="Website:", font=("Arial", 13))
entry_app = tk.Entry(root, font=("Arial", 13))
button_add = tk.Button(root, text="Add Password", command=add_password, font=("Arial", 13))
button_generate = tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 13))
label_fetch = tk.Label(root, text="Index, login or application:", font=("Arial", 13))
entry_fetch = tk.Entry(root, font=("Arial", 13))
button_fetch = tk.Button(root, text="Retrieve Password", command=retrieve_password, font=("Arial", 13))
button_clear = tk.Button(root, text="Clear Database", command=clear_database, font=("Arial", 13))
label_index = tk.Label(root, text="", font=("Arial", 13))
label_retrieved_password = tk.Label(root, text="", font=("Arial", 13))
button_copy_login = tk.Button(root, text="Copy Login", command=copy_login, font=("Arial", 13))
button_copy_password = tk.Button(root, text="Copy Password", command=copy_password, font=("Arial", 13))

# Place UI components on the background using grid and center them
label_login.grid(row=3, column=0)
entry_login.grid(row=3, column=1)
label_password.grid(row=4, column=0)
entry_password.grid(row=4, column=1)
label_app.grid(row=5, column=0)
entry_app.grid(row=5, column=1)
button_add.grid(row=6, column=1)
button_generate.grid(row=6, column=0)
label_fetch.grid(row=7, column=0)
entry_fetch.grid(row=7, column=1)
button_fetch.grid(row=8, column=1)
label_index.grid(row=10, column=0)
label_retrieved_password.grid(row=11, column=0)
button_copy_login.grid(row=3, column=2)
button_copy_password.grid(row=4, column=2)
button_clear.grid(row=11, column=1)


root.mainloop()