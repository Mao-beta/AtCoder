import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
    A = NLI()
    T = A[0] * 1000 + A[1] * 100 + A[2]
    Db = NI()
    B = NLI()
    Dc = NI()
    C = NLI()
    dp = [[[0]*10001 for _ in range(101)] for _ in range(11)]
    XYZ = [[x, y, z] for x in range(11) for y in range(101) for z in range(10001) if x*1000+y*100+z <= T]
    XYZ.sort(key=lambda x: x[0]*1000+x[1]*100+x[2])
    for x, y, z in XYZ:
        total = x * 1000 + y * 100 + z

        if total >= Db:
            tmp = Db
            dx = min(x, tmp // 1000)
            tmp -= dx * 1000
            dy = min(y, tmp // 100)
            tmp -= dy * 100
            if z >= tmp:
                dz = tmp
                dp[x][y][z] = max(dp[x-dx+B[0]][y-dy+B[1]][z-dz+B[2]] + 1, dp[x][y][z])

        if total >= Dc:
            tmp = Dc
            dx = min(x, tmp // 1000)
            tmp -= dx * 1000
            dy = min(y, tmp // 100)
            tmp -= dy * 100
            if z >= tmp:
                dz = tmp
                dp[x][y][z] = max(dp[x-dx+C[0]][y-dy+C[1]][z-dz+C[2]] + 1, dp[x][y][z])

        # if dp[x][y][z] > 0:
        #     print(x, y, z, total, dp[x][y][z])

    print(dp[A[0]][A[1]][A[2]])


if __name__ == "__main__":
    main()
