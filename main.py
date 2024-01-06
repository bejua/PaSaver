import tkinter as tk
import sqlite3
import pyperclip


# Establish the database connection
conn = sqlite3.connect('passappbase.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS passappbase (id INTEGER PRIMARY KEY AUTOINCREMENT, password TEXT, application TEXT)''')
conn.commit()


# Function to execute SQL queries
def execute_query(query, *args):
    c.execute(query, args)
    conn.commit()


# Function to add password to the database
def add_password():
    execute_query('INSERT INTO passappbase (password, application) VALUES (?, ?)', entry_password.get(), entry_application.get())
    label_index.config(text=f"New password added. Index: {c.lastrowid}")


# Function to retrieve password from the database
def retrieve_password():
    index_or_app = entry_index_or_app.get()
    c.execute('''SELECT password FROM passappbase WHERE id = ? OR application = ?''', (index_or_app, index_or_app))
    result = c.fetchone()
    if result:
        label_retrieved_password.config(text=f"Password: {result[0]}", fg="green")
        pyperclip.copy(result[0])
    else:
        label_retrieved_password.config(text="Not found", fg="red")


# Function to clear the entire database
def clear_database():
    execute_query('''DELETE FROM passappbase''')
    execute_query('''DELETE FROM SQLITE_SEQUENCE WHERE name='passappbase' ''')
    label_index.config(text="Database cleared")
    entry_password.delete(0, tk.END)
    entry_application.delete(0, tk.END)
    entry_index_or_app.delete(0, tk.END)
    label_retrieved_password.config(text="")


# GUI setup
root = tk.Tk()
root.title("Password Storage")
root.geometry("940x490")
root.resizable(False, False)


# Load the background image
background_image = tk.PhotoImage(file="vault.png")


# Create a label with the image and place it at the back of the window
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


# UI components
label_instruction = tk.Label(root, text="Enter password:", font=("Arial", 30), bg="#b86a39")
entry_password = tk.Entry(root, show="*", font=("Arial", 30))
label_instruction2 = tk.Label(root, text="Enter application:", font=("Arial", 30), bg="#b86a39")
entry_application = tk.Entry(root, font=("Arial", 30))
button_add = tk.Button(root, text="Add Password", command=add_password, font=("Arial", 20), bg="#b86a39")
label_index_or_app_instruction = tk.Label(root, text="Enter index or application:", font=("Arial", 30), bg="#b86a39")
entry_index_or_app = tk.Entry(root, font=("Arial", 30))
button_retrieve = tk.Button(root, text="Retrieve Password", command=retrieve_password, font=("Arial", 20), bg="#b86a39")
button_clear = tk.Button(root, text="Clear Database", command=clear_database, font=("Arial", 20), bg="#b86a39")
label_index = tk.Label(root, text="", font=("Arial", 30), bg="#b86a39")
label_retrieved_password = tk.Label(root, text="", font=("Arial", 30), bg="#b86a39")


# Place UI components on the background using grid and center them
label_instruction.grid(row=0, column=0)
entry_password.grid(row=0, column=1, padx=10)
label_instruction2.grid(row=1, column=0)
entry_application.grid(row=1, column=1, padx=10)
button_add.grid(row=2, column=0, columnspan=2, pady=5)
label_index_or_app_instruction.grid(row=3, column=0)
entry_index_or_app.grid(row=3, column=1, padx=10)
button_retrieve.grid(row=4, column=0, columnspan=2, pady=5)
button_clear.grid(row=5, column=0, columnspan=2, pady=5)
label_index.grid(row=6, column=0, columnspan=2)
label_retrieved_password.grid(row=7, column=0, columnspan=2)


root.mainloop()