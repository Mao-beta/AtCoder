import sys
import math
from collections import deque
from collections import Counter
sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    id, N, K = NMI()
    grid = [list(map(int, list(SI()))) for _ in range(N)]
    #print(grid)

    start_dic = {}
    seen = [[0] * N for _ in range(N)]
    for h in range(N):
        for w in range(N):
            if seen[h][w]: continue

            stack = deque()
            start = (h, w)
            #print(start)
            start_dic[start] = grid[h][w]
            stack.append(start)
            seen[start[0]][start[1]] = 1
            DIR = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            while stack:
                x, y = stack.pop()
                now_c = grid[x][y]
                for dx, dy in DIR:
                    if not(0 <= x+dx < N and 0 <= y+dy < N): continue
                    if seen[x+dx][y+dy]: continue
                    if grid[x+dx][y+dy] == now_c:
                        stack.append((x+dx, y+dy))
                        seen[x + dx][y + dy] = 1
    #print(seen)
    #print(start_dic)
    cnts = Counter(start_dic.values()).items()
    #print(cnts)
    max_c, max_x = list(cnts)[0]
    print(len(start_dic) - max_x)
    for p, c in start_dic.items():
        h, w = p
        if c == max_c: continue
        print(h+1, w+1, max_c)

if __name__ == "__main__":
    main()