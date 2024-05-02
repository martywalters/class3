import random
from concurrent.futures import ThreadPoolExecutor

def load_names(filename):
    """
    Load names from a text file and return the list.
    """
    with open(filename, 'r') as filehandle:
        return [name.rstrip() for name in filehandle.readlines()]

def generate_people(count):
    # Load first names and last names concurrently
    with ThreadPoolExecutor(max_workers=2) as executor:
        first_names_future = executor.submit(load_names, 'FirstNames.txt')
        last_names_future = executor.submit(load_names, 'LastNames.txt')

        first_names = first_names_future.result()
        last_names = last_names_future.result()

    # Generate random name tuples
    names = [(i, random.choice(first_names), random.choice(last_names)) for i in range(count)]

    return names

if __name__ == "__main__":
    people = generate_people(5)
    print(people)
