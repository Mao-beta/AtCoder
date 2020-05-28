from _collections import deque
H, W = map(int, input().split())
maze = []
wall = 0
for i in range(H):
    s = input()
    maze.append(s)
    wall += s.count('#')

queue = deque()
queue.append([0,0])
steps = [[-1]*W for _ in range(H)]
steps[0][0] = 0
while queue:
    now = queue.popleft()
    #print("now=" + str(now))

    UDLR = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for direction in UDLR:
        goto_y = now[0] + direction[0]
        goto_x = now[1] + direction[1]
        if (goto_x - 0)*(W-1 - goto_x) < 0 or (goto_y - 0)*(H-1 - goto_y) < 0:
            continue
        if maze[goto_y][goto_x] == '#' or steps[goto_y][goto_x] >= 0:
            continue

        queue.append([goto_y, goto_x])
        steps[goto_y][goto_x] = steps[now[0]][now[1]] + 1

#print("\n".join(map(str, steps)))
if steps[H-1][W-1] == -1:
    print(-1)
    exit()

print(H*W - wall - steps[H-1][W-1] - 1)