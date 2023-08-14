# -*- coding: utf-8 -*-
"""
2021-03-12
"""
from numpy import arange

sum_of_squares = []
for i in arange(1, 101):
    sum_of_squares.append(i**2)
    
print(sum(sum_of_squares) - sum(arange(1, 101))**2)