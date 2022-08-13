import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

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


def main():
    N = NI()
    C = [NLI() for _ in range(1<<N)]

    # 完全二分木のノード(1, ... (1<<N)-1)を考える
    # ノードi以下で誰も優勝しないときの最大値
    f = [0] * (1<<N)
    # i回戦で選手jが勝ち残っているときの最大値
    g = [[0] * (1<<N) for _ in range(N+1)]


    def rec(i, d, l, r):
        # d回戦の頂点i（[l, r)に対応）

        if d == 1:
            for x in range(l, r):
                f[i] = max(f[i], C[x][d-1])

            return

        m = (l+r) // 2

        rec(2*i, d-1, l, m)
        rec(2*i+1, d-1, m, r)

        # print(i, d, l, r)
        for x in range(l, m):
            # 左から来たxが勝ち上がる
            g[d][x] = max(g[d][x], g[d-1][x] + f[2*i+1])
            # ここで敗れる
            f[i] = max(f[i], g[d][x] + C[x][d-1])

        for x in range(m, r):
            # 右から来たxが勝ち上がる
            g[d][x] = max(g[d][x], g[d-1][x] + f[2*i])
            # ここで敗れる
            f[i] = max(f[i], g[d][x] + C[x][d-1])

    rec(1, N, 0, 1<<N)
    # print(f)
    # print(*g ,sep="\n")
    print(max(f))


if __name__ == "__main__":
    main()
