n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

d = {}
min_diff = n 

for i in range(n):
    if a[i] in d:
        min_diff = min(i - d[a[i]], min_diff) 
        d[a[i]] = i
        if min_diff == 1:
            break
    else:
        d[a[i]] = i

if min_diff == n:  
    print(-1)
else:
    print(min_diff)
