from functools import reduce

print('Lab4 Part 3 Extra Credit...')
# Define the compose function
def compose(*functions):
    return reduce(lambda f, g: lambda x: g(f(x)), functions)

# Metric system conversion functions
def cm_to_mm(cm):
    return cm * 10

def mm_to_cm(mm):
    return mm * 0.1

def mm_to_um(mm):
    return mm * 1000

def um_to_mm(um):
    return um * 0.001

def um_to_angstrom(um):
    return um * 10000

def angstrom_to_um(angstrom):
    return angstrom * 0.0001

# Define unit conversion compositions
cm_to_um = compose(mm_to_um, cm_to_mm)
um_to_cm = compose(mm_to_cm, um_to_mm)
um_to_angstrom = compose(angstrom_to_um, um_to_mm)

# Test the conversions
conversions = [
    ("cm to mm", cm_to_mm(5), 50),
    ("mm to cm", mm_to_cm(20), 2),
    ("mm to μm", mm_to_um(0.5), 500),
    ("μm to mm", um_to_mm(2000), 2),
    ("μm to Å", um_to_angstrom(3), 30000),
]

for conversion in conversions:
    print(f"{conversion[0]}: {conversion[1]} (expected: {conversion[2]})")
