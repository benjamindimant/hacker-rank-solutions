n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))

left = []
equal = ar[0]
right = []

for i in range(1, n):
    if ar[i] < equal:
        left.append(ar[i])
    else:
        right.append(ar[i])

print(*(left + [equal] + right))
