from threading import Semaphore, Thread, Lock
from queue import Queue, Empty
from random import randint
from time import sleep


max_customers_in_bank = 10 # maximum number of customers that can be in the bank at one time
max_customers = 30 # number of customers that will go to the bank today
max_tellers = 3 # number of tellers working today
teller_timeout = 10 # longest time that a teller will wait for new customers


class Customer:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"{self.name}"

# Example usage:
customer1 = Customer("Alice")
customer2 = Customer("Bob")

print(customer1)  # Output: Alice
print(customer2)  # Output: Bob

class Teller:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"{self.name}"

# Example usage:
teller1 = Teller("John")
teller2 = Teller("Jane")

print(teller1)  # Output: John
print(teller2)  # Output: Jane

import threading

def bankprint(lock, msg):
    with lock:
        print(msg)

# Example usage:
lock = threading.Lock()

# Create some messages
msg1 = "Hello, world!"
msg2 = "Welcome to the bank."

# Print messages using bankprint() function
bankprint(lock, msg1)
bankprint(lock, msg2)

def wait_outside_bank(customer, guard, teller_line, printlock):
    bankprint(printlock, f"(C) {customer.name} is waiting outside the bank")
    guard.acquire()
    bankprint(printlock, f"<G> Security guard lets {customer.name} into the bank")
    bankprint(printlock, f"(C) {customer.name} is trying to get into line")
    teller_line.put(customer)

def teller_job(teller, guard, teller_line, printlock):
    bankprint(printlock, f"[T] {teller.name} has started work")
    while True:
        try:
            customer = teller_line.get(timeout=3)  # Adjust timeout as needed
            bankprint(printlock, f"[T] {teller.name} is now helping {customer.name}")
            #sleep(random.uniform(1, 4))
            #sleep(2)
            bankprint(printlock, f"[T] {teller.name} is done helping {customer.name}")
            bankprint(printlock, f"<G> Security guard is letting {customer.name} out of the bank")
            guard.release()
        except queue.Empty:
            bankprint(printlock, f"[T] {teller.name} is going on break")
            break

if __name__ == "__main__":
    printlock = threading.Lock()
    teller_line = Queue(maxsize=max_customers_in_bank)
    guard = threading.Semaphore(max_customers_in_bank)

    bankprint(printlock, "<G> Security guard starting their shift")
    bankprint(printlock, "*B* Bank open")

    # Create customers
    for i in range(max_customers_in_bank):
        customer = Customer(f"Customer_{i+1}")
        thread = threading.Thread(target=wait_outside_bank, args=(customer, guard, teller_line, printlock))
        thread.start()

    sleep(5)

    bankprint(printlock, "*B* Tellers are going to start working now")
    tellers = [Teller(f"Teller_{i+1}") for i in range(max_customers_in_bank)]
    teller_threads = [threading.Thread(target=teller_job, args=(teller, guard, teller_line, printlock)) for teller in tellers]

    for thread in teller_threads:
        thread.start()

    for thread in teller_threads:
        thread.join()

    bankprint(printlock, "*B* Bank closed")
