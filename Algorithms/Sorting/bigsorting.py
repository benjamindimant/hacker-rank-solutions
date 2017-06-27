import sys

n = int(input().strip())
unsorted = []
for _ in range(n):
    unsorted_t = str(input().strip())
    unsorted.append(unsorted_t)
# your code goes here
buckets = {}
for i in unsorted:
    length = len(i)
    
    if length not in buckets:
        buckets[length] = []
    
    buckets[length].append(i)
    
for key in sorted(buckets):
    for i in sorted(buckets[key]):
        print(i)
