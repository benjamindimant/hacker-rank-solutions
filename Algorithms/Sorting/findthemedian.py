n = int(input())
ar = sorted(list(map(int, input().strip().split(' '))))

print(ar[len(ar) // 2])
