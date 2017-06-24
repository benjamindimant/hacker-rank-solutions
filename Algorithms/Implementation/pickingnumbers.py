import sys

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

maximum  = 0
for i in a:
    c1 = a.count(i)
    c2 = a.count(i - 1)
    c = c1 + c2
    if c > maximum:
        maximum = c
print(maximum)
