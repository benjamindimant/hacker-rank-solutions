import sys

def get_num_chocolates(m, w, count):
    if w >= m:
        return get_num_chocolates(m, w % m + w // m, count + w // m)
    else:
        return count   

t = int(input().strip())
for a0 in range(t):
    n,c,m = input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]
    count = n // c
    print(get_num_chocolates(m, count, count))
