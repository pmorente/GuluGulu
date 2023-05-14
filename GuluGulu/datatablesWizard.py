import sqlite3

def insert_pdfs_to_database(db_name, pdf_names, pdf_data):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS databasePDF
                  (id TEXT PRIMARY KEY NOT NULL,
                  name TEXT NOT NULL,
                  pdf_data TEXT NOT NULL);''')

    for i in range(len(pdf_names)):
        name = pdf_names[i]
        path = pdf_data[i]

        unique_id = generate_unique_id(7)
        c.execute("INSERT INTO databasePDF (id, name, pdf_data) VALUES (?, ?, ?)", (unique_id, name, path))
         
    conn.commit()
    conn.close()

    #print_database_data()

def generate_unique_id(length):
    import random
    import string

    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str

def print_id_and_name_from_database():
     # Open a connection to the database
    conn = sqlite3.connect('fib_gei.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Select all columns from the "databasePDF" table
    cursor.execute("SELECT id, name, pdf_data FROM databasePDF")

    # Fetch all rows
    rows = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Print the rows
    for row in rows:
        print(row[0], row[1], row[2])






pdf_names = ["Introducción a la Teoria de Grafos", "Todo lo que tienes que saber de M1", "Examen M1 2022 Primavera", "Examen M1 2021 Primavera", "Examen M1 2022 Otoño", "Examen M1 2021 Otoño", "Álgebra Lineal M2 Guía"]
pdf_data = ["pdf1.pdf"] * len(pdf_names)  # assumes all PDFs are in the same directory as pdf1.pdf
db_name = "fib_gei.db"

insert_pdfs_to_database(db_name, pdf_names, pdf_data)
print_id_and_name_from_database()
