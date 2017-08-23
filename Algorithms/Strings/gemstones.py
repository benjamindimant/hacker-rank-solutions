import sys

def gemstones(arr):
    elements = set(arr[0])
    if len(arr) > 1:
        for x in arr:
            elements = elements.intersection(set(x))
    return len(elements)

n = int(input().strip())
arr = []
arr_i = 0
for arr_i in range(n):
   arr_t = str(input().strip())
   arr.append(arr_t)
result = gemstones(arr)
print(result)
