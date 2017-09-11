def gameOfThrones(s):
    if len([c for c in set(s) if s.count(c) % 2 != 0]) < 2:
        return 'YES'
    return 'NO'
        

s = input().strip()
result = gameOfThrones(s)
print(result)
