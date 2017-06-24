import sys

def sockMerchant(n, ar):
    buffer = []
    count = 0
    for s in ar:
        if s in buffer:
            buffer.remove(s)
            count += 1
        else:
            buffer.append(s)
    return count

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
