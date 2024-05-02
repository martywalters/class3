print('Lab5 P1')
import random

def generate_people(count):
    # Load first names from FirstNames.txt
    with open('FirstNames.txt', 'r') as first_file:
        first_names = [name.rstrip() for name in first_file.readlines()]

    # Load last names from LastNames.txt
    with open('LastNames.txt', 'r') as last_file:
        last_names = [name.rstrip() for name in last_file.readlines()]

    # Generate random name tuples
    names = [(i, random.choice(first_names), random.choice(last_names)) for i in range(count)]

    return names

if __name__ == "__main__":
    people = generate_people(5)
    print(people)


