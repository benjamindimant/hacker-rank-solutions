def minSteps(n, B):
    return B.count('010') #count does not use the same character in substrings e.g. 01010 has '010' occur once
        
n = int(input().strip())
B = input().strip()
result = minSteps(n, B)
print(result)
