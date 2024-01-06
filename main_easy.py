import tkinter as tk

passwords = []

def add_password():
    password = entry_password.get()
    passwords.append(password)
    index = len(passwords) - 1
    label_index.config(text=f"Password saved. Index: {index}")

def retrieve_password():
    try:
        #1
        index = int(entry_index.get())
        #2
        password = passwords[index]
        #3
        label_retrieved_password.config(text=f"Password: {password}")
        #4
        label_retrieved_password2.config(text=f"Password: {password}")

    except IndexError:
        label_retrieved_password.config(text="Invalid index. Maybe, you introduced a too big index.")
    except ValueError:
        label_retrieved_password.config(text="You entered wrong index. Please, enter a number")


##############################################################

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
label_retrieved_password2 = tk.Label(root, text="")


label_instruction.pack()
entry_password.pack()
button_add.pack()
label_index_instruction.pack()
entry_index.pack()
button_retrieve.pack()
label_index.pack()
label_retrieved_password.pack()
label_retrieved_password2.pack()

root.mainloop()