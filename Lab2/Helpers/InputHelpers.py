__all__ = ['inputInt', 'inputFloat', 'inputString', 'inputDate']
from datetime import datetime
from Helpers.DataTypeHelpers import *
def inputInt(prompt = "Enter an integer: ", min_value = 0, max_value = 100):
    while True:
        s = input(prompt)
        if isInt(s):
            parsed_int = int(s)
            if min_value <= parsed_int <= max_value:
                return parsed_int
            else:
                print(f"Value {parsed_int} is out of range ({min_value} to {max_value}).")
            
        else:
            print("Entered text needs to be in int format. Please try again.")

def inputFloat(prompt = "Enter a float: ", min_value = 0, max_value = 100):
    while True:
        float_value =  input(prompt)
        if isFloat(float_value):
            parsed_float = float(float_value)
            if min_value <= parsed_float <= max_value:
                return float_value
            else:
                print(f"Value is out of range. Please enter a float between {min_value} and {max_value}.")
        else:
            print("Entered text needs to be in float format. Please try again.")

def inputString(prompt = "Enter a string: ", min_length = 0, max_length = 100):
    while True:
    #input will validate string
        try:
            string_value =  input(prompt)
            string_len = len(string_value)
            if min_length <= string_len <= max_length:
                return string_value
            else:
                print("Text must be between 5 and 10 in length")
        except ValueError:
            print("Entered text needs to be in string. Please try again.")

def inputDate(prompt = "Enter a date in ISO format (yyyy-mm-dd): "):
    while True:
        date_value =  input(prompt)
        if isDate(date_value):
                return (datetime.fromisoformat(date_value))
                #return date_value
        else:
            print("text needs to be in the “yyyy-mm-dd” format")
