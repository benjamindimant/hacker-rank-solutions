t = int(input().strip())
for _ in range(t):
    b,w = input().strip().split(' ')
    b,w = [int(b),int(w)]
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]

    min_cost = 0
    
    if x > y + z:
        min_cost += b * (y + z)
    else:
        min_cost += b * x
        
    if y > x + z:
        min_cost += w * (x + z)
    else:
        min_cost += w * y
        
    print(min_cost)
