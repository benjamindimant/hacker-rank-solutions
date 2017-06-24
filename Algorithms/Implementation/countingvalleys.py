import sys

def get_num_valleys(ar):
    valleys = 0
    cur_level = 0
    for c in ar:
        if c == 'U':
            cur_level += 1
            if cur_level == 0:
                valleys += 1
        else:
            cur_level -= 1
    return valleys

n = int(input().strip())
ar = list(input().strip())
result = get_num_valleys(ar)
print(result)
