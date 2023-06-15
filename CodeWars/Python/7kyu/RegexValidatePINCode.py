import re

from numpy import number 

def validate_pin(pin):
   
    return bool(re.fullmatch("\d{4}|\d{6}", pin))
   


print(validate_pin("1475"))