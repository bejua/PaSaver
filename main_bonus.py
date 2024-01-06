import tkinter as tk
import sqlite3
import pyperclip


conn = sqlite3.connect('passwords.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS Passwords (id INTEGER PRIMARY KEY AUTOINCREMENT, password TEXT)''')
conn.commit()

def add_password():
    password = entry_password.get()
    c.execute('''INSERT INTO Passwords (password) VALUES (?)''', (password,))
    conn.commit()
    label_index.config(text=f"Password saved. Index: {c.lastrowid}")

def retrieve_password():
    try:
        index = int(entry_index.get())
        c.execute('''SELECT password FROM Passwords WHERE id = ?''', (index,))
        result = c.fetchone()
        if result:
            label_retrieved_password.config(text=f"Password: {result[0]}")
            global retrieved_password
            retrieved_password = result[0]
        else:
            label_retrieved_password.config(text="Invalid index")
    except ValueError:
        label_retrieved_password.config(text="Enter a number")

def copy_to_clipboard():
    try:
        pyperclip.copy(retrieved_password)
        label_copy_status.config(text="Password copied to clipboard")
    except NameError:
        label_copy_status.config(text="No password retrieved yet")


root = tk.Tk()
root.title("Password Storage")
root.config(padx=100, pady=50)


label_instruction = tk.Label(root, text="Enter password:")
entry_password = tk.Entry(root, show="*")
button_add = tk.Button(root, text="Add Password", command=add_password)

label_index_instruction = tk.Label(root, text="Enter index:")
entry_index = tk.Entry(root)
button_retrieve = tk.Button(root, text="Retrieve Password", command=retrieve_password)

label_index = tk.Label(root, text="")
label_retrieved_password = tk.Label(root, text="")
button_copy = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
label_copy_status = tk.Label(root, text="")


label_instruction.pack()
entry_password.pack()
button_add.pack()
label_index_instruction.pack()
entry_index.pack()
button_retrieve.pack()
label_index.pack()
label_retrieved_password.pack()
button_copy.pack()
label_copy_status.pack()


root.mainloop()
