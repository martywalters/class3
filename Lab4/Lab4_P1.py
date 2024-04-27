from Fraction import *
from decimal import *

# Pi out to 50 digits
pi50 = Decimal("3.14159265358979323846264338327950288419716939937510")
# Number of iterations to perform
iterations = 1000000
#iterations = 1000

class LeibnizPiIterator:
    def __init__(self):
        self.fraction = Fraction(0, 1)
        self.n = 1
        self.add_next = True
    
    def __iter__(self):
        pass
    
    def __next__(self):
        if self.add_next:
            self.fraction += Fraction(4, self.n)
        else:
            self.fraction -= Fraction(4, self.n)
        self.add_next = not self.add_next
        self.n += 2
        return self.fraction

# Test the Iterator
print(f"pi after {iterations} iterations:", end=' ')
pi_iterator = LeibnizPiIterator()
for _ in range(iterations):
    pi_value = next(pi_iterator)
    if iterations % 100000 == 0: print(pi_value) # print the value every 100000 iterations

print(pi_value)

# Calculate the difference
difference = pi_value - pi50
print("Difference:", difference)

# Change iterations variable to 10,000,000 and re-run the test
iterations = 10000000
#iterations = 1000
print(f"\npi after {iterations} iterations:", end=' ')
pi_iterator = LeibnizPiIterator()
for _ in range(iterations):
    pi_value = next(pi_iterator)
print(pi_value)

# Calculate the difference
difference = pi_value - pi50
print("Difference:", difference)

        
