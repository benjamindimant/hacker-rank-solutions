import sys

def getRecord(s):
    records = [0, 0]
    curr_highest = s[0]
    curr_lowest = s[0]
    for i in s[1:]:
        if i > curr_highest:
            curr_highest = i
            records[0] += 1
        if i < curr_lowest:
            curr_lowest = i
            records[1] += 1
    return records
        

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))

