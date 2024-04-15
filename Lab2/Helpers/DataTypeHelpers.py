__all__ = ["isInt", "isFloat", "isDate" ]

#Intermediate Python Programming - Lab2 Sean Walters
from datetime import date

def isInt(value):
    abs_value= value.lstrip('+-')
    #print(f'{value} {abs_value}')
    if (abs_value.isnumeric()):
        #print('isnumeric')
        return True
    else:
        print('not numeric')
        return False
   
def isFloat(value):
    try:
        float(value)
        return True
    #except ValueError:
    except:
        return False
def isDate(value):
    try:
        #datetime.strptime(value, '%Y-%m-%d')
        date.fromisoformat(value)
        return True
    #except ValueError:
    except:
        return False

##added test but not sure the input statment doesn't complete it for me.
##def isString(value):
##    if type(value) is str:
##        return True
##    else:
##        return False
