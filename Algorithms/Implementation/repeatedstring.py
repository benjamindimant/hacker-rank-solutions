import sys

s = input().strip()
n = int(input().strip())

print((n // len(s)) * s.count('a') + s[0:(n % len(s))].count('a'))
