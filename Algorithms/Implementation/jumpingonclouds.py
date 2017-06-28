import sys

n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

curr_cloud = 0
num_jumps = 0

while (curr_cloud != n - 1):
    if (curr_cloud < n - 2 and c[curr_cloud + 2] == 0):
        curr_cloud += 2
    else:
        curr_cloud += 1
    num_jumps += 1

print(num_jumps)
