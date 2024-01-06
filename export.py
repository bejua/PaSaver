import sqlite3
import os

def export_data_to_txt():
    base_filename = 'exported_data.txt'
    if os.path.exists(base_filename):
        i = 2
        while True:
            new_filename = f'exported_data({i}).txt'
            if not os.path.exists(new_filename):
                break
            i += 1
    else:
        new_filename = base_filename

    conn = sqlite3.connect('passappbase.db')
    c = conn.cursor()

    with open(new_filename, 'w') as file:
        c.execute('SELECT application, login, password FROM passappbase')
        data = c.fetchall()

        for row in data:
            file.write(f"{row[0]} | {row[1]} | {row[2]}\n")

    conn.close()

export_data_to_txt()
