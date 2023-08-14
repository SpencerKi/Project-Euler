# -*- coding: utf-8 -*-
"""
2021-03-17
"""
from numpy import genfromtxt
grid = genfromtxt("P13.txt")
print(sum(grid)/1e42)