import tkinter as tk
import sqlite3

conn = sqlite3.connect('passappbase.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS passappbase (id INTEGER PRIMARY KEY AUTOINCREMENT, password TEXT, application TEXT)''')
conn.commit()

def add_password():
    password = entry_password.get()
    application = entry_application.get()
    c.execute('''INSERT INTO passappbase (password, application) VALUES (?, ?)''', (password, application))
    conn.commit()
    label_index.config(text=f"Password saved. Index: {c.lastrowid}")

def retrieve_password():
    try:
        index_or_app = entry_index_or_app.get()
        if index_or_app.isdigit():
            c.execute('''SELECT password FROM passappbase WHERE id = ?''', (index_or_app,))
        else:
            c.execute('''SELECT password FROM passappbase WHERE application = ?''', (index_or_app,))
        
        result = c.fetchone()
        if result:
            label_retrieved_password.config(text=f"Password: {result[0]}")
        else:
            label_retrieved_password.config(text="Not found")
    except ValueError:
        label_retrieved_password.config(text="Enter a valid index or application")

root = tk.Tk()
root.title("Password Storage")
root.config(padx=100, pady=50)

label_instruction = tk.Label(root, text="Enter password:")
entry_password = tk.Entry(root, show="*")
label_instruction2 = tk.Label(root, text="Enter application:")
entry_application = tk.Entry(root)
button_add = tk.Button(root, text="Add Password", command=add_password)

label_index_or_app_instruction = tk.Label(root, text="Enter index or application:")
entry_index_or_app = tk.Entry(root)
button_retrieve = tk.Button(root, text="Retrieve Password", command=retrieve_password)

label_index = tk.Label(root, text="")
label_retrieved_password = tk.Label(root, text="")

label_instruction.pack()
entry_password.pack()
label_instruction2.pack()
entry_application.pack()
button_add.pack()
label_index_or_app_instruction.pack()
entry_index_or_app.pack()
button_retrieve.pack()
label_index.pack()
label_retrieved_password.pack()

root.mainloop()
