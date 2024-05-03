#Part 1
import random

#Part 1 Extra Credit
import concurrent.futures

#Part 2
import sqlite3
people_db_file = "sqlite.db"  # The name of the database file to use
max_people = 500  # Number of records to create

#Part 4
import concurrent.futures

#Part 1
def generate_people(count):
    # Initialize empty lists for first and last names
    last_names = []
    first_names = []
    
    # Read last names from file
    with open('LastNames.txt', 'r') as filehandle:
        last_names = [name.rstrip() for name in filehandle.readlines()]

    # Read first names from file
    with open('FirstNames.txt', 'r') as filehandle:
        first_names = [name.rstrip() for name in filehandle.readlines()]
    
    # Generate list of random people tuples
    names = [(i, random.choice(first_names), random.choice(last_names)) for i in range(count)]
    
    return names

#Part 1 Extra Credit

def load_names(filename):
    with open(filename, 'r') as file:
        names = [name.strip() for name in file.readlines()]
    return names
def load_names_concurrently(count):
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        # Submit tasks for loading names from each file
        future_last_names = executor.submit(load_names, 'LastNames.txt')
        future_first_names = executor.submit(load_names, 'FirstNames.txt')

        # Retrieve results
        last_names = future_last_names.result()
        first_names = future_first_names.result()

    names = [(i, random.choice(first_names), random.choice(last_names)) for i in range(count)]
    return names

#Part 2
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

            # from Part 1 
            #people = generate_people(count)

            # from Part 1 Extra Credit
            people = load_names_concurrently(count)

            # Create query to add the people records
            sql_insert_person = "INSERT INTO people(id, first_name, last_name) VALUES(?, ?, ?);"
            for person in people:
                cursor.execute(sql_insert_person, person)

            cursor.close()
    
    except Error as e:
        print(e)
        
#Part 3

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

# Function to test the PersonDB class
def test_PersonDB():
    # Using a "with" block with a PersonDB object
    with PersonDB(people_db_file) as db:
        # Attempt to load and print three person records
        print(db.load_person(10000))  # Should print the default
        print(db.load_person(122))
        print(db.load_person(300))


#Part 4
def load_person(id, db_file):
    with PersonDB(db_file) as db:
        return db.load_person(id)
def load_all_people():
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        # Submit tasks for loading all people records
        future_records = [executor.submit(load_person, id, people_db_file) for id in range(max_people)]
        
        # Wait for all futures to complete
        concurrent.futures.wait(future_records)
        
        # Get results from completed futures
        records = [future.result() for future in future_records]
        
        return records

if __name__ == "__main__":
    #Part 1 test -----
    people = generate_people(5)
    print(people)

    #Part 1 Extra Credit
    names = load_names_concurrently(5)
    print(names)

    #Part 2
    create_people_database(people_db_file, max_people)

    #Part 3
    test_PersonDB()

    #Part 4
    all_people = load_all_people()
    print(all_people)

    #Part 4 Extra Credit
    sorted_people = sorted(all_people, key=lambda x: (x[2], x[1]))  # Sort by last name, then first name
    print(sorted_people)
    
    
