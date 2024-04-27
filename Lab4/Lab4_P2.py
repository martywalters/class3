from Fraction import *
from decimal import Decimal
pi50 = Decimal("3.14159265358979323846264338327950288419716939937510")

def NilakanthaPiGenerator():
    fraction = Fraction(3, 1)
    num = 2
    add_next = True
    
    while True:
        operand = Fraction(4, (num * (num + 1) * (num + 2)))
        if add_next:
            fraction += operand
        else:
            fraction -= operand
        add_next = not add_next
        num += 2
        yield fraction

# Test the Generator
def test_nilakantha_pi(iterations):
    print(f"pi after {iterations} iterations:", end=' ')
    pi_generator = NilakanthaPiGenerator()
    for _ in range(iterations):
        pi_value = next(pi_generator)
    print(pi_value)

    # Calculate the difference
    difference = pi_value - pi50
    print("Difference:", difference)

# Set iterations to 100,000 and test
iterations = 100000
test_nilakantha_pi(iterations)

# Change iterations variable to 10,000,000 and re-run the test
iterations = 10000000
test_nilakantha_pi(iterations)
