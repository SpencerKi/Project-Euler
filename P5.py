# -*- coding: utf-8 -*-
"""
2021-03-11
"""
from numpy import arange

def twen_div(num: int) -> bool:
    """Returns True iff num evenly divisible by all integers [1,20].
    """
    for i in arange(1, 21):
        if num % i != 0:
            return False
    return True

##Original solution
#def twen_div_range(num: int) -> int:
#    """Finds smallest integer in range num divisible by all integers [1,20].
#    """
#    for i in range(2520, num):
#        if twen_div(i):
#            return(i)
    
x = 2520 #Given in question: 2520 smallest int evenly divisible by [1,10].
while not twen_div(x):
    x += 20
print(x)