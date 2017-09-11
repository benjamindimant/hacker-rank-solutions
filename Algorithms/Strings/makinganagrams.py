import sys

def makingAnagrams(s1, s2):
    s1_dict = {}
    for c in s1:
        try:
            s1_dict[c] += 1
        except:
            s1_dict[c] = 1
    s2_dict = {}
    for c in s2:
        try:
            s2_dict[c] += 1
        except:
            s2_dict[c] = 1
    deletions = 0
    for c in set(s1_dict.keys()).union(set(s2_dict.keys())):
        if c in s1_dict.keys() and c in s2_dict.keys():
            deletions += abs(s1_dict[c] - s2_dict[c])
        elif c in s1_dict.keys() and c not in s2_dict.keys():
            deletions += s1_dict[c]
        else:
            deletions += s2_dict[c]
            
    return deletions
            
s1 = input().strip()
s2 = input().strip()
result = makingAnagrams(s1, s2)
print(result)
