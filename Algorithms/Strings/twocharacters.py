def is_alternate(string):
    if len(string) == 1:
      return False
    elif len(string) == 2:
        if string[0] == string[1]:
            return False
        else:
            return True
    else:
        for i in range(2, len(string), 2):
            if string[i] != string[0] or string[i] == string[i - 1]:
                return False
        for j in range(1, len(string), 2):
            if string[j] != string[1] or string[j] == string[j - 1]:
                return False
        return True

s_len = int(input().strip())
s = input().strip()

maximum = 0

pairs = []
chars = list(set(s))
if len(chars) > 2:
    for i in range(len(chars)):
        for j in range(i, len(chars)):
            if chars[i] != chars[j]:
                pairs.append((chars[i], chars[j]))
    for cs in pairs:
        temp_str = "".join([x for x in s if x == cs[0] or x == cs[1]])
        if is_alternate(temp_str):
            maximum = max(maximum, len(temp_str))
else:
    if is_alternate(s):
        maximum = max(maximum, len(s))
    
print(maximum)
