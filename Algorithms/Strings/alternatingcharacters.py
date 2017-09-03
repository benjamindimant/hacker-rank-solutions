def alternatingCharacters(s):
    num = 0
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            num += 1
    return(num)

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = alternatingCharacters(s)
    print(result)
