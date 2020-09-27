import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    H, W = NMI()
    grid = [SI() for _ in range(H)]
    step = [[-1]*W for _ in range(H)]
    que = deque()
    for h in range(H):
        for w in range(W):
            p = grid[h][w]
            if p == "#":
                que.append((h, w))
                step[h][w] = 0
    DIR = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    while que:
        x, y = que.popleft()

        for dx, dy in DIR:
            if not(0 <= x+dx < H and 0 <= y+dy < W):
                continue
            if step[x+dx][y+dy] >= 0:
                continue
            que.append((x+dx, y+dy))
            step[x+dx][y+dy] = step[x][y] + 1

    print(max([max(s) for s in step]))



if __name__ == "__main__":
    main()