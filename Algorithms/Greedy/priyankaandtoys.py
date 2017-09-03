n = int(input())
w = set(map(int, input()strip().split(' ')))

i = 0
while len(w) > 0:
    i += 1
    m = min(w)
    w = W.difference(set(range(m, m + 5)))

print(i)
