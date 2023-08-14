# -*- coding: utf-8 -*-
"""
2021-03-17

Functional, but too inefficient.
"""
import numpy as np

def factor_count(num: int) -> int:
    """Returns number of divisors of integer num.
    
    Precondition: num > 1
    """
    factors = 2
    for i in np.arange(2, (num // 2) + 1):
        if num % i == 0:
            factors += 1
    return factors

num_factors = 0
count = 1
tri_num = 0
while num_factors < 500:
    tri_num += count
    count += 1
    num_factors = factor_count(tri_num)
    
print(tri_num)