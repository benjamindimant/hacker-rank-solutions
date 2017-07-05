p = int(input().strip())
q = int(input().strip())

k_nums = []

for i in range(p, q + 1):
    d = len(str(i))
    i_squared = str(i * i)
    r = i_squared[-d:]
    l = i_squared[:d] if len(i_squared) % 2 == 0 else i_squared[:d - 1]
    sum_l_r = int(r)
    if l != '':
        sum_l_r += int(l)
    if sum_l_r == i:
        k_nums.append(sum_l_r)

if (k_nums):
    print(*k_nums)
else:
    print("INVALID RANGE")
