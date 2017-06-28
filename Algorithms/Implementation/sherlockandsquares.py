import math

t = int(input())

def is_sqrt(n):
    sqrt = math.sqrt(n)
    return (sqrt - math.floor(sqrt)) == 0

for _ in range(t):
    a, b = map(int, input().strip().split(' '))
    sqrt_a = math.ceil(math.sqrt(a))
    sqrt_b = math.floor(math.sqrt(b))
    print(sqrt_b - sqrt_a + 1)
