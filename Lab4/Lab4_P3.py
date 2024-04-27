from functools import reduce

# Define the compose function
def compose(*functions):
    return reduce(lambda f, g: lambda x: g(f(x)), functions)

# Distance conversion functions
def miles_to_yards(miles):
    return miles * 1760

def yards_to_miles(yards):
    return yards * 0.0005681818181818

def yards_to_feet(yards):
    return yards * 3

def feet_to_yards(feet):
    return feet * 0.3333333333333333

def feet_to_inches(feet):
    return feet * 12

def inches_to_feet(inches):
    return inches * 0.0833333333333333

def inches_to_cm(inches):
    return inches * 2.54

def cm_to_inches(cm):
    return cm * 0.3937007874015748

def cm_to_meters(cm):
    return cm * 0.01

def meters_to_cm(meters):
    return meters * 100

def meters_to_kilometers(meters):
    return meters * 0.001

def kilometers_to_meters(kilometers):
    return kilometers * 1000

def kilometers_to_au(kilometers):
    return kilometers * 0.000000006684587122268445

def au_to_kilometers(au):
    return au * 149597870.700

def au_to_ly(au):
    return au * 0.00001581250740982065847572

def ly_to_au(ly):
    return ly * 63241.07708426628026865358

# Define unit conversion compositions
miles_to_inches = compose(feet_to_inches, yards_to_feet, miles_to_yards)
feet_to_meters = compose(cm_to_meters, meters_to_cm, inches_to_cm, feet_to_inches)
meter_to_inches = compose(feet_to_inches, cm_to_inches)
miles_to_kilometers = compose(meters_to_kilometers, kilometers_to_meters, miles_to_yards)
kilometers_to_miles = compose(yards_to_miles, miles_to_yards, kilometers_to_meters)
kilometers_to_inches = compose(feet_to_inches, yards_to_feet, miles_to_yards, kilometers_to_meters)
inches_to_kilometers = compose(meters_to_kilometers, meter_to_inches)
meters_to_ly = compose(au_to_ly, kilometers_to_au, meters_to_kilometers)

# Test the conversions
conversions = [
    ("miles to inches", miles_to_inches(2), 126720),
    ("feet to meters", feet_to_meters(5), 1.524),
    ("meter to inches", meter_to_inches(1), 39.37007874015748),
    ("miles to kilometers", miles_to_kilometers(10), 16.09344),
    ("kilometers to miles", kilometers_to_miles(1), 0.6213711922373341),
    ("kilometers to inches", kilometers_to_inches(12.7), 500000.0),
    ("inches to kilometers", inches_to_kilometers(500000), 12.7),
    ("meters to light years", meters_to_ly(9_460_730_472_580_800), 1)
]

for conversion in conversions:
    print(f"{conversion[0]}: {conversion[1]} (expected: {conversion[2]})")
