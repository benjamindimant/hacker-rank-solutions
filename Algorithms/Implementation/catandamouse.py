import sys

n = int(input().strip())
queries = []
for i in range(0, n):
    query = list(map(int, input().strip().split(' ')))
    queries.append(query)

for q in queries:
    x = q[0]
    y = q[1]
    z = q[2]
    if (abs(x - z) == abs(y - z)):
        print("Mouse C")
    elif (abs(x - z) < abs(y - z)):
        print("Cat A")
    else:
        print("Cat B")
