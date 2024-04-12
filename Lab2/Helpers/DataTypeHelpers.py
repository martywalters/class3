__all__ = ["isInt", "isFloat", "isDate", "isString" ]

import datetime

def isInt(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
    
def isFloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
def isDate(value):
    try:
        datetime.datetime.strptime(value, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# added test but not sure the input statment doesn't complete it for me.
def isString(value):
    if type(value) is str:
        return True
    else:
        return False
