from Fraction import *
from decimal import *

# Pi out to 50 digits
pi50 = Decimal("3.14159265358979323846264338327950288419716939937510")
# Number of iterations to perform
iterationsLong = 10000000
iterations = 100000
print('Lab4 Part 1...')
class LeibnizPiIterator:
    def __init__(self):
        pass
    
    def __iter__(self):
        self.fraction = Fraction(0, 1)
        self.n = 1
        self.add_next = True
        return self
    
    def __next__(self):
     
        if self.add_next:
            self.fraction += Fraction(4, self.n)
        else:
            self.fraction -= Fraction(4, self.n)
        
        self.add_next = not self.add_next
        self.n += 2
        return self.fraction

# Test iterations to 100,000 
pi_iterator = LeibnizPiIterator()
#iterator = iter(pi_iterator)
iterator = iter(pi_iterator)
for pi_counter in range(iterations):
    pi_iterator = next(iterator)
difference = abs(pi_iterator.value - pi50)
print(f"pi after {iterations} iterations: {pi_iterator.value:2.50f}")
print(f"Difference: { difference:2.50f}")

# Test iterations to 10,000,000
pi_iterator = LeibnizPiIterator()
iterator = iter(pi_iterator)
for pi_counter in range(iterationsLong):
    pi_iterator = next(iterator)
difference = abs(pi_iterator.value - pi50)
print(f"pi after {iterationsLong} iterations: {pi_iterator.value:2.50f}")
print(f"Difference: { difference:2.50f}")




        
