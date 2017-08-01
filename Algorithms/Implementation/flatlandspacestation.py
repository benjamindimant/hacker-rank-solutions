n, m = input().strip().split(' ')
n, m = [int(n),int(m)]
c = sorted([int(c_temp) for c_temp in input().strip().split(' ')])

distances = [c[0]] + [(((c[i] - c[i - 1])) // 2) for i in range(1, len(c))] + [(n - 1 - c[-1])]
try:
	print(max(distances))
except:
	print(0)
