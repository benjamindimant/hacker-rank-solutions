def fibonacci(n):
    return fib(0, 1, n)

def fib(fib1, fib2, n):
    if (n == 0):
        return fib1
    else:
        return fib(fib2, fib1 + fib2, n - 1)
        
n = int(input())
print(fibonacci(n))
