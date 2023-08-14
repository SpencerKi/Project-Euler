# -*- coding: utf-8 -*-
"""
2021-03-11
"""
def ex_div(num:int, div: int) -> int:
    """Divides until exhausted.
    """
    a = num
    while a % div == 0:
        a //= div
    return a

def big_prime(num: int) -> float:
    """Returns largest prime factor of integer num.
    """
    big = num
    fac = 2
    while big != fac:
        big = ex_div(big, fac)
        fac += 1
    return big