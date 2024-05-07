import sqlite3
from sqlite3 import Error

people_db_file = "sqlite.db"  # The name of the database file to use
max_people = 500  # Number of records to create

def create_people_database(db_file, count):
    # Create a connection to SQLite
    conn = sqlite3.connect(db_file)
    with conn:
        # Rest of the code will go here

sql_create_people_table = """
CREATE TABLE IF NOT EXISTS people (
    id integer PRIMARY KEY,
    first_name text NOT NULL,
    last_name text NOT NULL
);
"""
cursor = conn.cursor()
cursor.execute(sql_create_people_table)

sql_truncate_people = "DELETE FROM people;"
cursor.execute(sql_truncate_people)

people = generate_people(count)

sql_insert_person = "INSERT INTO people(id, first_name, last_name) VALUES(?, ?, ?);"
for person in people:
    # Uncomment the following lines if you want to see the person object and row ID
    # print(person)
    # print(cursor.lastrowid)
    cursor.execute(sql_insert_person, person)
cursor.close()


if __name__ == "__main__":
    create_people_database(people_db_file, max_people)
