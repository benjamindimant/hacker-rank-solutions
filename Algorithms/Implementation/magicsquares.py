#!/bin/python3

import sys

s = []
for s_i in range(3):
   s_t = [int(s_temp) for s_temp in input().strip().split(' ')]
   s.append(s_t)
#  Print the minimum cost of converting 's' into a magic square

n = [s[i][j] for i in range(3) for j in range(3)]    

all_n = [[8, 1, 6, 3, 5, 7, 4, 9, 2],
         [6, 1, 8, 7, 5, 3, 2, 9, 4],
         [4, 9, 2, 3, 5, 7, 8, 1, 6],
         [2, 9, 4, 7, 5, 3, 6, 1, 8],
         [8, 3, 4, 1, 5, 9, 6, 7, 2],
         [4, 3, 8, 9, 5, 1, 2, 7, 6],
         [6, 7, 2, 1, 5, 9, 8, 3, 4],
         [2, 7, 6, 9, 5, 1, 4, 3, 8]]

all_sum = []
for l in all_n:
    all_sum.append(sum([abs(n[i] - l[i]) for i in range(9)]))
print(min(all_sum))
