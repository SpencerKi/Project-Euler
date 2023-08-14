# -*- coding: utf-8 -*-
"""
2021-03-13, eventually solved 2021-03-16.
"""
import numpy as np

def is_prime(num: int) -> bool:
    """Returns True if integer num is prime and False otherwise.
    
    Precondition: num > 2, set has evens removed.
    """
    factors = []
    for i in np.arange(3, np.int64(np.sqrt(num)) + 1, 2, dtype = np.int64):
        if num % i == 0:
            factors.append(i)
    if factors == []:
        return True
    elif len(factors) > 0:
        return False
    else:
        return "ERROR"

sum_primes = np.int64(2)
for i in np.arange(3, 2000000, 2, dtype = np.int64):
    if is_prime(i):
        sum_primes += i
        
print(sum_primes)