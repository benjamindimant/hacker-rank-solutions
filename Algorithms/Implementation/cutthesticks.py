import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

while (arr):
    print(len(arr))
    arr = list(filter(lambda x: x > 0, list(map(lambda x: x - min(arr), arr))))
