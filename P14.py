# -*- coding: utf-8 -*-
"""
2021-03-17
"""
import numpy as np

def collatzer(num: int, length: int) -> int:
    """Apply Collatz conjecture algorithm to integer num for
    specified number of steps length.
    """
    new_num = num
    count = length
    while new_num > 1 and count > 0:
        if new_num % 2 == 0:
            new_num //= 2
            count -= 1
        else:
            new_num = 3 * new_num + 1
            count -= 1
    return new_num

def count_collatzer(num: int) -> int:
    """Apply Collatz conjecture algorithm to integer num and
    return the number of required steps to arrive at 1.
    """
    new_num = np.int64(num)
    count = 0
    while new_num > 1:
        if new_num % 2 == 0:
            new_num //= 2
            count += 1
        else:
            new_num = 3 * new_num + 1
            count += 1
    return count

longest = 0
long_count = 0
for i in np.arange(1,1000000):
    long = count_collatzer(i)
    if long > long_count:
        long_count = long
        longest = i
        
print(longest)

"""
Attempt 1
0 -> 1/2, 5 -> 3/2, 6 -> 3/4, 3 -> 9/4, 0
1 -> 3, 4 -> 3/2, 2 -> 3/4, 1
2 -> 1/2, 1 -> 3/2, 4 -> 3/4, 2
3 -> 3, 0 -> 3/2, 5 -> 9/2, 6 -> 9/4, 3
4 -> 1/2, 2 -> 1/4, 1 -> 3/4, 4
5 -> 3, 6 -> 3/2, 3 -> 9/2, 0 -> 9/4, 5
6 -> 1/2, 3 -> 3/2, 0 -> 3/4, 5 -> 9/4, 6
7 -> 
8 -> 
9 ->

Attempt 2
def collatzer(num: int, length: int) -> list:
    '''Finds 
    '''
    mult = 1
    unit = num
    count = length
    while count > 0:
        if unit % 2 == 0:
            if unit != 0:
                mult /= 2
                unit /= 2
            else:
                mult /= 2
                unit = 5
        else:
            mult *= 3
            unit = (3 * unit + 1) % 10
        count -= 1
    return [mult, unit]

Didn't realise that more than the last digit mattered.
"""