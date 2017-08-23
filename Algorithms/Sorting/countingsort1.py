count = [0] * 100

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
for i in ar:
    count[i] += 1
    
print(*count)
