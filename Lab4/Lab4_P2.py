from Fraction import *
from decimal import *
pi50 = Decimal("3.14159265358979323846264338327950288419716939937510")

rangeshort = 100000
rangelong  = 10000000

print('Lab4 Part 2...')

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


pi_generator_100k = NilakanthaPiGenerator()
for iterator in range(rangeshort):
    approximation = next(pi_generator_100k)

difference = abs(approximation.value - pi50)
print(f"pi after {rangeshort} iterations: {approximation.value:2.50f}")
print(f"Difference: { difference:2.50f}")


pi_generator_10000k = NilakanthaPiGenerator()
for iterator in range(rangelong):
    approximation = next(pi_generator_10000k)

difference = abs(approximation.value - pi50)
print(f"pi after {rangelong} iterations: {approximation.value:2.50f}")
print(f"Difference: { difference:2.50f}")


