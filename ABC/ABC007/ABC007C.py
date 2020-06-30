from _collections import deque
R, C = map(int, input().split())
start = list(map(lambda x: int(x) - 1, input().split()))
goal = list(map(lambda x: int(x) - 1, input().split()))
maze = []
for i in range(R):
    maze.append(input())

queue = deque()
queue.append(start)
steps = [[-1]*C for _ in range(R)]
steps[start[0]][start[1]] = 0
while queue:
    now = queue.popleft()
    #print("now=" + str(now))

    UDLR = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for direction in UDLR:
        goto_y = now[0] + direction[0]
        goto_x = now[1] + direction[1]
        if maze[goto_y][goto_x] == '#' or steps[goto_y][goto_x] >= 0:
            continue
        queue.append([goto_y, goto_x])
        steps[goto_y][goto_x] = steps[now[0]][now[1]] + 1

#print("\n".join(map(str, steps)))
print(steps[goal[0]][goal[1]])