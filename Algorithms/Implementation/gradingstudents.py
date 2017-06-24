#!/bin/python3

import sys

def round5(x):
    return x + 5 - (x % 5)

def solve(grades):
    for i in grades:
        if i >= 37:
            if (round5(i) - i) < 3: 
                i = round5(5)
    return grades

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
    grades_t = int(input().strip())
    grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
