import tkinter as tk
import sqlite3
import pyperclip

conn = sqlite3.connect('passappbase.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS passappbase (id INTEGER PRIMARY KEY AUTOINCREMENT, password TEXT, application TEXT)''')
conn.commit()

def execute_query(query, *args):
    c.execute(query, args)
    conn.commit()

def add_password():
    execute_query('INSERT INTO passappbase (password, application) VALUES (?, ?)', entry_password.get(), entry_application.get())
    label_index.config(text=f"New password added. Index: {c.lastrowid}")

def retrieve_password():
    index_or_app = entry_index_or_app.get()
    c.execute('''SELECT password FROM passappbase WHERE id = ? OR application = ?''', (index_or_app, index_or_app))
    result = c.fetchone()
    if result:
        label_retrieved_password.config(text=f"Password: {result[0]}", fg="green")
        pyperclip.copy(result[0])
    else:
        label_retrieved_password.config(text="Not found", fg="red")

def clear_database():
    execute_query('''DELETE FROM passappbase''')
    execute_query('''DELETE FROM SQLITE_SEQUENCE WHERE name='passappbase' ''')
    label_index.config(text="Database cleared")
    entry_password.delete(0, tk.END)  # Clear entry_password field
    entry_application.delete(0, tk.END)  # Clear entry_application field
    entry_index_or_app.delete(0, tk.END)  # Clear entry_index_or_app field
    label_retrieved_password.config(text="")  # Clear label_retrieved_password text

root = tk.Tk()
root.title("Password Storage")
root.geometry("400x380")
root.resizable(False, False)
root.config(padx=20, pady=20)

label_instruction = tk.Label(root, text="Enter password:", font=("Arial", 12))
entry_password = tk.Entry(root, show="*", font=("Arial", 12))
label_instruction2 = tk.Label(root, text="Enter application:", font=("Arial", 12))
entry_application = tk.Entry(root, font=("Arial", 12))
button_add = tk.Button(root, text="Add Password", command=add_password, font=("Arial", 12))

label_index_or_app_instruction = tk.Label(root, text="Enter index or application:", font=("Arial", 12))
entry_index_or_app = tk.Entry(root, font=("Arial", 12))
button_retrieve = tk.Button(root, text="Retrieve Password", command=retrieve_password, font=("Arial", 12))

button_clear = tk.Button(root, text="Clear Database", command=clear_database, font=("Arial", 12))
button_copy = tk.Button(root, text="Copy to Clipboard", command=lambda: pyperclip.copy(label_retrieved_password.cget("text")[10:]), font=("Arial", 12))

label_index = tk.Label(root, text="", font=("Arial", 12))
label_retrieved_password = tk.Label(root, text="", font=("Arial", 12))

label_instruction.pack()
entry_password.pack()
label_instruction2.pack()
entry_application.pack()
button_add.pack(pady=5)
label_index_or_app_instruction.pack()
entry_index_or_app.pack()
button_retrieve.pack(pady=5)
button_clear.pack(pady=5)
label_index.pack()
label_retrieved_password.pack()
button_copy.pack(pady=5)

root.mainloop()
