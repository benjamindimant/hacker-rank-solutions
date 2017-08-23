import sys

n = int(input().strip())
ar = sorted(list(set(map(int, input().strip().split(' ')))))
    
min_diff = sys.maxsize
min_pairs = []

for i in range(len(ar) - 1):
    if abs(ar[i] - ar[i+1]) < min_diff:
        min_pairs = [ar[i], ar[i+1]]
    elif abs(ar[i] - ar[i+1]) == min_diff:
        min_pairs.append(ar[i])
        min_pairs.append(ar[i+1])
    min_diff = min(abs(ar[i] - ar[i+1]), min_diff)
                      
print(*min_pairs)
