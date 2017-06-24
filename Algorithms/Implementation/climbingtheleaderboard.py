import sys

n = int(input().strip())
scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
m = int(input().strip())
alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]
# your code goes here
leaderboard = sorted(set(scores), reverse = True)
l = len(leaderboard)

for a in alice:
    while (l > 0) and (a >= leaderboard[l-1]):
        l -= 1
    print(l + 1)
