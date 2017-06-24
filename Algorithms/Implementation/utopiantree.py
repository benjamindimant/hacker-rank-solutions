import sys

t = int(input().strip())
nums = []
for a0 in range(t):
    n = int(input().strip())
    nums.append(n)
    
for i in nums:
    if i == 0:
        h = 1
    elif i % 2 == 0:
        h = int(2 ** ((i / 2) + 1) - 1)
    else:
        h = int(2 ** ((i + 3) / 2) - 2)
    print(h)
