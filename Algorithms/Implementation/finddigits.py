import sys

t = int(input().strip())
ints = []
for a0 in range(t):
    n = int(input().strip())
    ints.append(n)

for i in ints:
    count = 0
    digits = list(map(int, str(i)))
    for d in digits:
        if (d != 0 and i % d == 0):
            count += 1
    print(count)
