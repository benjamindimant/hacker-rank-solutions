n, k = map(int, input().strip().split(' '))

important_comps = []
max_luck = 0
for _ in range(n):
    l, t = map(int, input().strip().split(' '))
    if t == 1:
        important_comps.append(l)
    else:
        max_luck += l

important_comps.sort(reverse=True)
max_luck += sum(important_comps[:k]) - sum(important_comps[k:])
    
print(max_luck)
