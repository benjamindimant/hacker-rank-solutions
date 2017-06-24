#!/bin/python

import sys

def getTotalX(a, b):
    nums = set()
    for i in range(max(a), max(b) + 1):
        if (all(map(lambda x: i % x == 0, a)) and all(map(lambda x: x % i == 0, b))):
            nums.add(i)
    return len(nums)

n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
a = map(int, raw_input().strip().split(' '))
b = map(int, raw_input().strip().split(' '))
total = getTotalX(a, b)
print(total)
