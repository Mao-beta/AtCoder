H, W = map(int, input().split())
grid = [input() for _ in range(H)]
blacks = [[0]*W for _ in range(H)]

grid_to_num = {"#":1, ".":0}

blacks[0][0] = grid_to_num[grid[0][0]]
for j in range(1, W):
    blacks[0][j] = blacks[0][j-1] + grid_to_num[grid[0][j]] * (1-grid_to_num[grid[0][j-1]])
for i in range(1, H):
    blacks[i][0] = blacks[i-1][0] + grid_to_num[grid[i][0]] * (1-grid_to_num[grid[i-1][0]])
    for j in range(1, W):
        blacks[i][j] = blacks[i][j-1] + grid_to_num[grid[i][j]] * (1-grid_to_num[grid[i][j-1]])
        blacks[i][j] = min(blacks[i-1][j] + grid_to_num[grid[i][j]] * (1-grid_to_num[grid[i-1][j]]), blacks[i][j])

print(blacks[H-1][W-1])