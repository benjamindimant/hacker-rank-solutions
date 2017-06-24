import sys

def getMoneySpent(keyboards, drives, s):
    perms = [x + y for x in keyboards for y in drives]
    affordable = list(filter(lambda x: x <= s, perms))
    if not affordable:
        return -1
    return max(affordable)

s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
