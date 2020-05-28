H, W = map(int, input().split())
grid = [input() for _ in range(H)]
UDLR = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for i in range(H):
    for j in range(W):
        here = grid[i][j]
        if here == '.':
            continue
        ng = True
        for direction in UDLR:
            side_h = i + direction[0]
            side_w = j + direction[1]
            if 0 <= side_h < H and 0 <= side_w < W:
                side = grid[side_h][side_w]
                if side == '#':
                    ng = False
        if ng:
            print('No')
            exit()

print('Yes')