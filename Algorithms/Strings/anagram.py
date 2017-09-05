def anagram(s):
    count = 0
    s = list(s)
    l = len(s)
    if l % 2 != 0:
        return -1
    else:
        s1 = s[:l // 2]
        s2 = s[l // 2:]
        for i in s1:
            if i not in s2:
                count += 1
            else:
                s2.remove(i)
        return count

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = anagram(s)
    print(result)
