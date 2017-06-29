import sys

s = input().strip()

print(sum(map(str.isupper, s)) + 1)
