n = int(input().strip())

def calc_people(pop, count, x, n):
    count += pop // 2
    if (x == n):
        return count
    else:      
        return calc_people((pop // 2) * 3, count, x + 1, n)
    
print(calc_people(5, 0, 1, n))
