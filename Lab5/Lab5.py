print('Lab5 P1')
import random
import concurrent.futures
import sqlite3
from sqlite3 import Error

people_db_file = "sqlite.db"  # The name of the database file to use
max_people = 500  # Number of records to create



class PersonDB:
    def __init__(self, db_file=''):
        self.db_file = db_file

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_file)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.conn.close()

    def load_person(self, id):
        sql = "SELECT * FROM people WHERE id=?"
        cursor = self.conn.cursor()
        cursor.execute(sql, (id,))
        records = cursor.fetchall()
        result = (-1, '', '')  # Default record if not found
        if records is not None and len(records) > 0:
            result = records[0]
        cursor.close()
        return result




def create_people_database(db_file, count):
    try:
        # Create a connection to SQLite database
        conn = sqlite3.connect(db_file)

        # SQL command string to create the "people" table
        sql_create_people_table = """ CREATE TABLE IF NOT EXISTS people (
                                    id INTEGER PRIMARY KEY,
                                    first_name TEXT NOT NULL,
                                    last_name TEXT NOT NULL); """

        # Open a cursor and execute the command
        with conn:
            cursor = conn.cursor()
            cursor.execute(sql_create_people_table)

            # Truncate any existing data from the table
            sql_truncate_people = "DELETE FROM people;"
            cursor.execute(sql_truncate_people)

            # Generate list of person tuples
            people = generate_people(count)

            # Create query to add the people records
            sql_insert_person = "INSERT INTO people(id, first_name, last_name) VALUES(?, ?, ?);"
            for person in people:
                cursor.execute(sql_insert_person, person)

            cursor.close()
    
    except Error as e:
        print(e)


def generate_people(count):
    # Initialize empty lists for first and last names
    last_names = []
    first_names = []
    
    # Read last names from file
    with open('LastNames.txt', 'r') as filehandle:
        last_names = [name.strip() for name in filehandle.readlines()]

    # Read first names from file
    with open('FirstNames.txt', 'r') as filehandle:
        first_names = [name.strip() for name in filehandle.readlines()]
    
    # Generate list of random people tuples
    people = [(i, random.choice(first_names), random.choice(last_names)) for i in range(count)]
    
    return people

def read_names(filename):
    with open(filename, 'r') as file:
        names = [name.strip() for name in file.readlines()]
    return names

def load_names(filename):
    return read_names(filename)

def load_names_concurrently(count):
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        # Submit tasks for loading names from each file
        future_last_names = executor.submit(load_names, 'LastNames.txt')
        future_first_names = executor.submit(load_names, 'FirstNames.txt')

        # Retrieve results
        last_names = future_last_names.result()
        first_names = future_first_names.result()

        people = [(i, random.choice(first_names), random.choice(last_names)) for i in range(count)]
        
    return people
    #return first_names, last_names

def test_PersonDB():
    # Replace 'people_db_file' with the appropriate file name if needed
    with PersonDB(people_db_file) as db:
        print(db.load_person(10000))  # Should print the default
        print(db.load_person(122))
        print(db.load_person(300))

def load_person(id, db_file):
    with PersonDB(db_file) as db:
        return db.load_person(id)

def load_all_people(db_file):
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        # Submit tasks for loading all people records
        future_records = [executor.submit(load_person, id, db_file) for id in range(max_people)]
        
        # Wait for all futures to complete
        concurrent.futures.wait(future_records)
        
        # Get results from completed futures
        records = [future.result() for future in future_records]
        
        return records
    
def sort_records(records):
    return sorted(records, key=lambda x: (x[2], x[1]))  # Sort by last name then first name

if __name__ == "__main__":
    people = generate_people(5)
    print(people)
    print('------')
    #first_names, last_names = load_names_concurrently()
    people2 = load_names_concurrently(5)
    print (people2)
    #print("First Names:", first_names[:5])  # Print first 5 first names
    #print("Last Names:", last_names[:5])    # Print first 5 last names

    create_people_database(people_db_file, max_people)

    all_people = load_all_people(people_db_file)
    sorted_people = sort_records(all_people)
    print('Sorted people')
    print(sorted_people)

    test_PersonDB()

    
    print(all_people)


