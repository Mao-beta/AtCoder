import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD99 = 998244353

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())
EI = lambda m: [NLI() for _ in range(m)]


def main():
    N = NI()
    XY = EI(N)
    C = [[[-1, -1] for _ in range(2002)] for _ in range(2002)]
    DX = [-2, -1, 0, 1, 2] * 5
    DY = [-2] * 5 + [-1] * 5 + [0] * 5 + [1] * 5 + [2] * 5
    ans = 0
    for x, y in XY:
        xx, yy = x // 10, y // 10
        ok = True
        for dx, dy in zip(DX, DY):
            nx, ny = xx+dx, yy+dy
            if 0 <= nx < 2002 and 0 <= ny < 2002:
                cx, cy = C[nx][ny]
                if cx == cy == -1:
                    continue
                if (cx-x)**2 + (cy-y)**2 < 400:
                    ok = False
        if ok:
            C[xx][yy] = [x, y]
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
