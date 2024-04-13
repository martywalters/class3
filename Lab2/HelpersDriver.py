# test_driver.py
from Helpers import *
#from Helpers.DataTypeHelpers import *
#from Helpers.InputHelpers import *

#print(isInt('123.6'))
#print(isFloat('123.6'))

#print(isDate("2024-04-12"))
#print(isDate("2024-04-12T12:34:56"))

print(inputInt("Please enter a number: ", 0, 100))
print(inputFloat("Please enter a number: ", -10, 1000))
print(inputString("Enter some text: ", 5, 10))
print(inputDate("Enter a date: "))

##
##print(inputInt(min_value = 0, max_value = 100))
##print(inputFloat(min_value = 0, max_value = 100))
##print(inputString(min_length = 0, max_length = 100))
##print(inputDate("Enter a date: "))
