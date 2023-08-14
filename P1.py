# -*- coding: utf-8 -*-
"""
2021-03-11
"""
add = []
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        add.append(i)
print(sum(add))