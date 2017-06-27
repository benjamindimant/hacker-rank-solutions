def fib(f1, f2, n):
    if (n == 0):
        return f1
    else:
        return fib(f2, (f1 + f2 * f2), n - 1)
    
t1, t2, n = map(int, input().strip().split(' '))
print(fib(t1, t2, n - 1))
