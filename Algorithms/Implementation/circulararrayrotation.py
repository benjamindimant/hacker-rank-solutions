import sys


n,k,q = input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
indices = []
for a0 in range(q):
    m = int(input().strip())
    indices.append(m)
    
k = k % n
rotated = a[-k:] + a[:-k]
for i in indices:
    print(rotated[i])
