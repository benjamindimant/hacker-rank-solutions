q = int(input().strip())

def is_perm(a, b, n):
    for i in range(n):
        if a[i] + b[i] < k:
            return 'NO'
    return 'YES'

for _ in range(q):
    n, k = map(int, input().strip().split(' '))
    a = sorted(map(int, input().strip().split(' ')))
    b = sorted(map(int, input().strip().split(' ')), reverse = True)
    print(is_perm(a, b, n))
