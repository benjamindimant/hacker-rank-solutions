import sys

def migratoryBirds(n, ar):
    counts = [0, 0, 0, 0, 0]
    for i in ar:
        counts[i - 1] += 1
    return counts.index(max(counts)) + 1

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
