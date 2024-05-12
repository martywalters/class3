from threading import Semaphore, Thread, Lock
from queue import Queue, Empty
from random import randint
from time import sleep
import time
import random

max_customers_in_bank = 10  # maximum number of customers that can be in the bank at one time
max_customers = 30          # number of customers that will go to the bank today
max_tellers = 3             # number of tellers working today
teller_timeout = 10         # longest time that a teller will wait for new customers

class Customer:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"{self.name}"

class Teller:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"{self.name}"

def bankprint(lock, msg):
    with lock:
        print(msg)

def wait_outside_bank(customer, guard, teller_line, printlock):
    bankprint(printlock, f"(C) {customer} waiting outside bank")
    guard.acquire()
    bankprint(printlock, f"<G> Security guard letting {customer} into the bank")
    bankprint(printlock, f"(C) {customer} getting into line")
    teller_line.put(customer)

def teller_job(teller, guard, teller_line, printlock):
    bankprint(printlock, f"[T] {teller} starting work")

    while True:
        try:
            customer = teller_line.get(timeout=teller_timeout)
            bankprint(printlock, f"[T] {teller}  is now helping {customer}")
            time.sleep(random.randint(1, 4))
            bankprint(printlock, f"[T] {teller} is done helping {customer}")
            bankprint(printlock, f"<G> Security guard is letting {customer} out of the bank")
            guard.release()
        except Empty:
            bankprint(printlock, f"[T] {teller} is going on break")
            break
        

if __name__ == "__main__":
    printlock = Lock()
    teller_line = Queue(maxsize=max_customers_in_bank)
    guard = Semaphore(max_customers_in_bank)

    bankprint(printlock, "<G> Security guard starting their shift")
    bankprint(printlock, "*B* Bank open")

    customers = [Customer(f"Customer_{i+1}") for i in range(max_customers)]
    for customer in customers:
        t = Thread(target=wait_outside_bank, args=(customer, guard, teller_line, printlock))
        t.start()

    time.sleep(5)

    tellers = [Teller(f"Teller_{i+1}") for i in range(max_tellers)]
    teller_threads = [Thread(target=teller_job, args=(teller, guard, teller_line, printlock)) for teller in tellers]
    for t in teller_threads:
        t.start()
    for t in teller_threads:
        t.join()
    bankprint(printlock, "*B* Bank closed")
    
    
