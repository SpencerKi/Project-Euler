# -*- coding: utf-8 -*-
"""
2021-03-12
"""
from numpy import arange

def is_prime(num: int) -> bool:
    """Returns True if integer num is prime and False otherwise.
    
    Precondition: num > 2
    """
    if num % 2 == 0 and num != 2:
        return False
    else:
        factors = []
        for i in arange(1, num + 1, 2):
            if num % i == 0:
                factors.append(i)
        if len(factors) > 2:
            return False
        elif len(factors) == 2:
            return True
        else:
            return "ERROR"

primes = [2]
j = 3
while len(primes) < 10001:
    if is_prime(j):
        primes.append(j)
    j += 2
    
print(primes[-1])