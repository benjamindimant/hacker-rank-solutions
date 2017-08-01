import sys

q = int(input().strip())
target = 'hackerrank'
for _ in range(q):
    s = input().strip()
    index = 0
    for i in s:
        if target[index] == i:
            index += 1
        if index == len(target):
            print("YES")
            break
    if index != len(target):
        print("NO")
