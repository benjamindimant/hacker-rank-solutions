import sys

d1,m1,y1 = input().strip().split(' ')
d1,m1,y1 = [int(d1),int(m1),int(y1)]
d2,m2,y2 = input().strip().split(' ')
d2,m2,y2 = [int(d2),int(m2),int(y2)]

def calc_days_late(d1, d2):
    return 15 * (d1 - d2)

def calc_months_late(m1, m2):
    return 500 * (m1 - m2)

if (y1 > y2):
    print(10000)
elif (m1 > m2 and y1 == y2):
    print(calc_months_late(m1, m2))
elif (d1 > d2 and m1 == m2 and y1 == y2):
    print(calc_days_late(d1, d2))
else:
    print(0)
