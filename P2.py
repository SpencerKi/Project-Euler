# -*- coding: utf-8 -*-
"""
2021-03-11
"""
fibonacci = [1,2]
last_term = 2
while last_term < 4000000:
    last_term = fibonacci[-2] + fibonacci[-1]
    fibonacci.append(last_term)

sum = 0
for i in fibonacci[:-1]:
    if i % 2 == 0:
        sum += i
        
print(sum)