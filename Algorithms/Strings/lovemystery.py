def theLoveLetterMystery(s):
    changes = 0
    for i in range(len(s) // 2):
        changes += abs(ord(s[i]) - ord(s[-i - 1]))
    return changes

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = theLoveLetterMystery(s)
    print(result)
