n = int(input().strip())

o = []

for i in range(n):
    o.append((i + 1, sum(map(int, input().strip().split(' ')))))
    
print(*list(map(lambda x: x[0], sorted(o, key = lambda x: x[1]))))
