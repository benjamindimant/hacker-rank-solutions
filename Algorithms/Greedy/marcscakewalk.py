import sys

def get_exercise(l):
    total = 0
    for i in range(len(l)):
        total += 2 ** i * l[i]
    return total

n = int(input().strip())
calories = sorted(list(map(int, input().strip().split(' '))), reverse = True)
print(get_exercise(calories))
