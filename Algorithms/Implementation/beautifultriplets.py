n, d = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
count = 0

for i in range(n):
    if a[i] + d in a and a[i] + 2*d in a:
        count += 1
print(count)
