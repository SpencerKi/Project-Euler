# -*- coding: utf-8 -*-
"""
2021-03-12
"""
from numpy import sqrt

a = 1
while a + int(1000*(a - 500)/(a - 1000)) + int(sqrt(a**2 + 1000000*(a - 500)**2/(a - 1000)**2)) != 1000:
    a += 1

print(int(a * 1000*(a - 500)/(a - 1000) * sqrt(a**2 + 1000000*(a - 500)**2/(a - 1000)**2)))