from functools import reduce

print('Lab4 Part 3 Extra Credit...')
# Define the compose function
def compose(*functions):
    return reduce(lambda f, g: lambda x: g(f(x)), functions)

# Metric system conversion functions
def cmToMm(cm):
    return cm * 10

def mmToCm(mm):
    return mm * 0.1

def mmToUm(mm):
    return mm * 1000

def umToMm(um):
    return um * 0.001

def umToAngstrom(um):
    return um * 10000

def angstromToUm(angstrom):
    return angstrom * 0.0001

cmToUm = compose(mmToUm, cmToMm)
umToCm = compose(mmToCm, umToMm)
cmToAngstrom = compose(umToAngstrom,mmToUm, cmToMm)
angstromToCm = compose(mmToCm,umToMm,angstromToUm)
conversions = [
    ("cm to um",5, cmToMm(5), 50000),
    ("um to cm",10000, umToCm(10000), 1),
    ("cm to angstrom",3, cmToAngstrom(3), 300000000),
    ("angstrom to mm",2000000,angstromToCm(2000000),0.2)
]

for conversion in conversions:
    print(f"Convert {conversion[1]} {conversion[0]}: {conversion[2]} (expected: {conversion[3]})")
