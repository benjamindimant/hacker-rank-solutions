import sys

s = input().strip()
t = input().strip()
k = int(input().strip())

operations_left = k
while (operations_left >= 0):
    if s == t[:len(s)] and len(t) - len(s) == operations_left or len(s) == 0:
        break
    s = s[:-1]
    operations_left -= 1
print("Yes" if len(t) - len(s) <= operations_left else "No")
