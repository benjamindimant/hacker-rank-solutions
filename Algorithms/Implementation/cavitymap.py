n = int(input().strip())
grid = []
for _ in range(n):
   grid_t = list(str(input().strip()))
   grid.append(grid_t)
for i in range(1, n - 1):
    for j in range(1, n - 1):   
        if grid[i][j] > max(grid[i][j + 1], grid[i][j - 1], grid[i - 1][j], grid[i + 1][j]):
                grid[i][j] = 'X'
for i in grid:
    print("".join(i))
