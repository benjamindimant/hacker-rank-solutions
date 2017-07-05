import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# your code goes here
min_diff = sys.maxsize
a.sort()
for i in range(0, len(a) - 1):
    min_diff = min(min_diff, abs(a[i + 1] - a[i]))
    if min_diff == 0:
        break
print(min_diff)
