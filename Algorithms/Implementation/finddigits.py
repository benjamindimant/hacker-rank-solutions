import sys

t = int(input().strip())
ints = []
for a0 in range(t):
    n = int(input().strip())
    ints.append(n)
    
for i in ints:
    print(len([x for x in list(map(int, str(i))) if (x != 0) and (i % x == 0)]))
