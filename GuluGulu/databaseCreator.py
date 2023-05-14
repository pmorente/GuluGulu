import sqlite3

conn = sqlite3.connect('fib_gei.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE databasePDF
                  (id INT PRIMARY KEY NOT NULL,
                  name TEXT NOT NULL,
                  pdf_data TEXT NOT NULL);''')

conn.commit()
conn.close()