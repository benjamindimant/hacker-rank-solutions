import sys

s = input().strip()
n = int(input().strip())
u = set()
prev = '0'
count = 1
for c in s:
    if c == prev:
        count += 1
        u.add(count * (ord(c) - 96))
    else:
        u.add(ord(c) - 96)
        count = 1
        prev = c
for a0 in range(n):
    x = int(input().strip())
    # your code goes here
    print("Yes") if x in u else print("No")
