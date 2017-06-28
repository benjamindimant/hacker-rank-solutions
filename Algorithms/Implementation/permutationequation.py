n = int(input())
seq = list(map(int, input().strip().split(' ')))

for i in range(1, n + 1):
    print(seq.index(seq.index(i) + 1) + 1)
