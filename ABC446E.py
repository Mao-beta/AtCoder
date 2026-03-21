import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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
    M, A, B = NMI()
    dp = [[0]*M for _ in range(M)]
    ngs = [[0]*M for _ in range(M)]
    ans = 0
    for xy in range(M**2):
        x, y = divmod(xy, M)
        if dp[x][y]:
            continue
        if x == 0 or y == 0:
            dp[x][y] = 1
            ngs[x][y] = 1
            continue
        dp[x][y] = 1
        L = [xy]
        while True:
            nx, ny = divmod(L[-1], M)
            nz = (A * ny + B * nx) % M
            if ngs[ny][nz]:
                for xxyy in L:
                    xx, yy = divmod(xxyy, M)
                    ngs[xx][yy] = 1
                break
            if dp[ny][nz]:
                ans += len(L)
                break
            L.append(ny * M + nz)
            dp[ny][nz] = 1
    print(ans)


if __name__ == "__main__":
    main()
