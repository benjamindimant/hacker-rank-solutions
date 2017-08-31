import sys

def getMinimumCost(n, k, c):
    p = [0] * k
    for i in range(n - 1, -1, -1):
        p[i % k] += sorted(c)[i] * ((n - 1 - i) // k + 1)
    return sum(p)

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
c = list(map(int, input().strip().split(' ')))
minimumCost = getMinimumCost(n, k, c)
print(minimumCost)
