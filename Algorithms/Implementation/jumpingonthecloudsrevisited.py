import sys

n, k = input().strip().split(' ')
n, k = [int(n),int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]        

# Initialise
curr_cloud = 0
e = 100

#do
curr_cloud = (curr_cloud + k) % n
e -= 1
if c[curr_cloud] == 1:
    e -= 2

while curr_cloud != 0:
    curr_cloud = (curr_cloud + k) % n
    e -= 1
    if c[curr_cloud] == 1:
        e -= 2

print(e)
