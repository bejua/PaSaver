import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('database.db')  # Replace 'database.db' with your database name
cursor = conn.cursor()

# Retrieve data from the database
cursor.execute("SELECT * FROM database")  # Replace 'database' with your table name
data = cursor.fetchall()

# Get column names
cursor.execute("PRAGMA table_info(database)")  # Replace 'database' with your table name
columns = [col[1] for col in cursor.fetchall()]

# Create a DataFrame
df = pd.DataFrame(data, columns=columns)

# Export data to Excel
df.to_html('output.html', index=False)  # Save to 'output.xlsx'

# Close the database connection
conn.close()
