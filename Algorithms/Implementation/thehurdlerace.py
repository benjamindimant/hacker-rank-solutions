import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
height = list(map(int, input().strip().split(' ')))
required = max(height)
num_drinks = 0 if (required <= k) else (required - k)
print(num_drinks)
