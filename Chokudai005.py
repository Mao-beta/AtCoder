import sys
import math
from collections import deque

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
    cnts = [0]*10
    for row in grid:
        for x in row:
            cnts[x] += 1
    max_x = cnts.index(max(cnts))
    max_c = max(cnts)
    print(N**2 - max_c)
    for h in range(N):
        for w in range(N):
            if grid[h][w] != max_x:
                print(h+1, w+1, max_x)



if __name__ == "__main__":
    main()