# test_driver.py

from Helpers.DataTypeHelpers import *
from Helpers.InputHelpers import *

#print(isInt('123.6'))
#print(isFloat('123.6'))

#print(isDate("2024-04-12"))
#print(isDate("2024-04-12T12:34:56"))

print(inputInt("Please enter a number: ", 0, 100))
print(inputFloat("Please enter a number: ", -10, 1000))
print(inputString("Enter some text: ", 5, 10))
print(inputDate("Enter a date: "))
