import sys

n = int(input().strip())
s = input().strip()
k = int(input().strip())

print("".join(list(map(lambda x: chr((ord(x) - ord('a') + k) % 26 + ord('a')) if x.islower() else chr((ord(x) - ord('A') + k) % 26 + ord('A')) if x.isupper() else x, s))))
