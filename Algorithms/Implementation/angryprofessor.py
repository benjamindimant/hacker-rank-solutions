import sys

t = int(input().strip())
s = []
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    s.append((k, a))

for z in s:
    if len(list(filter(lambda x: x <= 0, z[1]))) >= z[0]:
        print("NO")
    else:
        print("YES")
