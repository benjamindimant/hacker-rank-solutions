#!/bin/python3

import sys

def is_happy(b):
    for i in set(b):
        if b.count(i) == 1 and i != '_':
            return 'NO'
        elif i == '_' and b.count(i) == len(b):
            return 'YES'
    if b.count('_') == 0:
        for i in range(1,len(b)-1):
            if b[i] != b[i+1] and b[i] != b[i-1]:
                return 'NO'
    return 'YES'

Q = int(input().strip())
for a0 in range(Q):
    n = int(input().strip())
    b = list(input().strip())
    print(is_happy(b))
    


