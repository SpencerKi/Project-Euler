# -*- coding: utf-8 -*-
"""
2021-03-11
"""

def is_pal(num: int) -> bool:
    return str(num) == str(num)[::-1]

largest = 0

for i in reversed(range(1000)):
    for j in reversed(range(1000)):
        if is_pal(i*j) and i*j > largest:
            largest = i*j