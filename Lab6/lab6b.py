from threading import Thread, Semaphore, Lock
from queue import Queue, Empty  # Import Empty exception
import random
import time

max_customers_in_bank = 5
max_tellers = 2
teller_timeout = 2

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
    bankprint(printlock, f"(C) {customer} is waiting outside the bank")
    guard.acquire()
    bankprint(printlock, f"<G> Security guard let {customer} into the bank")
    bankprint(printlock, f"(C) {customer} is trying to get into line")
    teller_line.put(customer)

def teller_job(teller, guard, teller_line, printlock):
    bankprint(printlock, f"[T] {teller} starts working")
    while True:
        try:
            customer = teller_line.get(timeout=teller_timeout)
            bankprint(printlock, f"[T] {teller} is helping {customer}")
            time.sleep(random.randint(1, 4))
            bankprint(printlock, f"[T] {teller} is done helping {customer}")
            bankprint(printlock, f"<G> Security guard is letting {customer} out of the bank")
            guard.release()
        except Empty:  # Catch Empty exception
            bankprint(printlock, f"[T] {teller} is going on break")
            break

if __name__ == "__main__":
    printlock = Lock()
    teller_line = Queue(maxsize=max_customers_in_bank)
    guard = Semaphore(max_customers_in_bank)

    bankprint(printlock, "<G> Security guard starting their shift")
    bankprint(printlock, "*B* Bank open")

    customers = [Customer(f"Customer_{i+1}") for i in range(max_customers_in_bank)]
    for customer in customers:
        t = Thread(target=wait_outside_bank, args=(customer, guard, teller_line, printlock))
        t.start()

    time.sleep(5)

    bankprint(printlock, "*B* Tellers are going to start working now")
    tellers = [Teller(f"Teller_{i+1}") for i in range(max_tellers)]
    teller_threads = [Thread(target=teller_job, args=(teller, guard, teller_line, printlock)) for teller in tellers]
    for t in teller_threads:
        t.start()
    
    for t in teller_threads:
        t.join()

    bankprint(printlock, "*B* Bank closed")
