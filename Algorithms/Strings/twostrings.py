def twoStrings(s1, s2):
    if set(s1).isdisjoint(set(s2)):
        return 'NO'
    return 'YES'

q = int(input().strip())
for a0 in range(q):
    s1 = input().strip()
    s2 = input().strip()
    result = twoStrings(s1, s2)
    print(result)

# [s2[i:j+1] for i in xrange(len(s2)) for j in xrange(i, len(s2))] returns all substirngs in O(n^2)
