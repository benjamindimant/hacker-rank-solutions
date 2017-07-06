import sys

def funnyString(s):
    # Complete this function
    for i in range(1, len(s)):
        if (abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(s[len(s) - i]) - ord(s[len(s) - i - 1]))):
            return "Not Funny"
    return "Funny"
    
q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = funnyString(s)
    print(result)
