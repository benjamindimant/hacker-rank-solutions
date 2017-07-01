import sys

def super_reduced_string(s):
    has_adj_chars = True
    while (has_adj_chars):
        init_length = len(s)
        curr_length = len(s)
        index = 0
        while (index < curr_length - 1):
            if s[index] == s[index + 1]:
                s = s[:index] + s[index + 2:]
                curr_length -= 2
            else:
                index += 1
        if curr_length == init_length:
            has_adj_chars = False
    if len(s) == 0:
        return "Empty String"
    else:
        return s

s = input().strip()
result = super_reduced_string(s)
print(result)
