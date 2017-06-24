import sys

def bonAppetit(n, k, b, ar):
    del ar[k]
    actual = int(sum(ar) / 2)
    if (actual == b):
        return "Bon Appetit"
    return b - actual

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
