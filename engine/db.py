import csv
import sqlite3

con = sqlite3.connect("jarvis.db")
cursor = con.cursor()

# query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'PowerPoint','C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.exe')"
# cursor.execute(query)
# con.commit()

# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
# cursor.execute(query)
# query = "INSERT INTO web_command VALUES (null,'youtube','https://www.youtube.com/')"
# cursor.execute(query)
# con.commit()

#texting module.............
# app_name = "android studio"
# cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
# results = cursor.fetchall()
# print(results)

# Create a table with the desired columns
# cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')



# # Specify the column indices you want to import (0-based index)
# desired_columns_indices = [0, 28]

# # Read data from CSV and insert into SQLite table for the desired columns
# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
    
#     # Skip header if the CSV has one (optional)
#     next(csvreader, None)

#     for row in csvreader:
#         # Ensure row has enough columns before accessing indices
#         if len(row) > max(desired_columns_indices):
#             selected_data = [row[i] for i in desired_columns_indices]
#             cursor.execute('''INSERT INTO contacts (id, name, mobile_no) VALUES (NULL, ?, ?);''', tuple(selected_data))
#         else:
#             print(f"Skipping row due to missing columns: {row}")

# # Commit changes and close connection
# con.commit()
# con.close()

