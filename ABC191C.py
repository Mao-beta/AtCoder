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
    ans = 0
    for h in range(H-1):
        for w in range(W-1):
            LU = grid[h][w]
            LD = grid[h+1][w]
            RU = grid[h][w+1]
            RD = grid[h+1][w+1]
            A = [LU, LD, RU, RD]
            if A.count("#") % 2:
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
