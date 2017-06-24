import sys

h = list(map(int, input().strip().split(' ')))
word = input().strip()
letter_heights = list(map(lambda x: h[ord(x) - 97], word))
print(max(letter_heights) * len(word))
