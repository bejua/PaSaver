import tkinter as tk

passwords = []

def addpass():
    password = password_entry.get()
    passwords.append(password)
    password_entry.delete(0, tk.END)  # Clear the entry field after adding password
    result_label.config(text=f"Password added at index {len(passwords) - 1}", fg="black")

def retrievepass():
    try:
        index = int(index_entry.get())
        if 0 <= index < len(passwords):
            result_label2.config(text=f"Password at index {index}: {passwords[index]}", fg="black")
        else:
            result_label2.config(text="Invalid index", fg="red")
    except ValueError:
        result_label2.config(text="Please enter a valid index", fg="red")

# Create the main window
root = tk.Tk()
root.title("Password Storage")
root.config(padx=100, pady=50)

# Password Entry
password_label = tk.Label(root, text="Enter Password:")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Add Password Button
add_button = tk.Button(root, text="Add Password", command=addpass)
add_button.pack()

# Index Entry
index_label = tk.Label(root, text="Enter Index:")
index_label.pack()

index_entry = tk.Entry(root)
index_entry.pack()

# Retrieve Password Button
retrieve_button = tk.Button(root, text="Retrieve Password", command=retrievepass)
retrieve_button.pack()

# Result Label
result_label = tk.Label(root, text="", fg="black")
result_label.pack()

# Result Label
result_label2 = tk.Label(root, text="", fg="black")
result_label2.pack()

# Run the Tkinter event loop
root.mainloop()