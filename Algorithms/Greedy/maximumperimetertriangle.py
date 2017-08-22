n = int(input().strip())
sticks = sorted(list(map(int, input().strip().split(' '))))
                
i = n - 3

while i >= 0 and sticks[i] + sticks[i+1] <= sticks[i+2]:
    i -= 1

if i < 0:
    print(-1)
else:
    print(sticks[i], sticks[i+1], sticks[i+2])
