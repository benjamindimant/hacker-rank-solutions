import sys

s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

num_apples = 0
for appl in apple:
    if ((appl + a) in range(s, t)):
        num_apples += 1

num_oranges = 0
for orng in orange:
    if ((orng + b) in range(s, t)):
        num_oranges += 1

print(num_apples)
print(num_oranges)
