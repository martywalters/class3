from functools import reduce

print('Lab4 Part 3...')
# Define the compose function
def compose(*functions):
    return reduce(lambda f, g: lambda x: g(f(x)), functions)

# Distance conversion functions
def milesToYards(miles):
    return miles * 1760
def yardsToMiles(yards):
    return yards * 0.0005681818181818
def yardsToFeet(yards):
    return yards * 3
def feetToYards(feet):
    return feet * 0.3333333333333333
def feetToInches(feet):
    return feet * 12
def inchesToFeet(inches):
    return inches * 0.0833333333333333
def inchesToCm(inches):
    return inches * 2.54
def cmToInches(cm):
    return cm * 0.3937007874015748
def cmToMeters(cm):
    return cm * 0.01
def metersToCm(meters):
    return meters * 100
def metersToKm(meters):
    return meters * 0.001
def kmToMeters(kilometers):
    return kilometers * 1000
def kmToMeters(kilometers):
    return kilometers * 1000
def kmToAu(kilometers):
    return kilometers * 0.000000006684587122268445
def auToKm(au):
    return au * 149597870.700
def auToLy(au):
    return au * 0.00001581250740982065847572
def lyToAu(ly):
    return ly * 63241.07708426628026865358

# Define unit conversion compositions

milesToInches = compose(feetToInches, yardsToFeet, milesToYards)
feet_to_meters = compose(cmToMeters, inchesToCm, feetToInches)
meter_to_inches = compose(cmToInches,metersToCm)
miles_to_kilometers = compose(metersToKm,cmToMeters,inchesToCm,feetToInches, yardsToFeet, milesToYards) 
kilometers_to_miles = compose(yardsToMiles,feetToYards, inchesToFeet,cmToInches,metersToCm, kmToMeters) #  error 
kilometers_to_inches = compose(cmToInches, metersToCm, kmToMeters) # error
inches_to_kilometers = compose(metersToKm,cmToMeters, inchesToCm)
meters_to_ly = compose(auToLy, kmToAu, metersToKm)

# Test the conversions
conversions = [
    ("miles to inches",2, milesToInches(2), 126720),
    ("feet to meters",5, feet_to_meters(5), 1.524),
    ("meter to inches",1, meter_to_inches(1), 39.37007874015748),
    ("miles to kilometers",10, miles_to_kilometers(10), 16.09344),
    ("kilometers to miles",1,kilometers_to_miles(1), 0.6213711922373341),
    ("kilometers to inches",12.7, kilometers_to_inches(12.7), 500000.0),
    ("inches to kilometers",500000, inches_to_kilometers(500000), 12.7),
    ("meters to light years",'9,460,730,472,580,800', meters_to_ly(9_460_730_472_580_800), 1)
]
for conversion in conversions:
    print(f"Convert {conversion[1]} {conversion[0]}  (result: {conversion[2]})")
