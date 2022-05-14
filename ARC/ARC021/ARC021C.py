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
    K = NI()
    N = NI()
    AD = [NLI() for _ in range(N)]

    def calc_buy(a, d, c):
        if a > c:
            return 0, 0, 0, 0

        xl = (c - a) // d + 1
        sl = (a + a+d*(xl-1)) * xl // 2
        x, s = 0, 0
        if (c - a) % d == 0:
            sl -= a+d*(xl-1)
            s += a+d*(xl-1)
            xl -= 1
            x = 1

        return xl, sl, x, s

    ans = 10**20
    ok = 10**20
    ng = -1

    while abs(ok-ng) > 1:
        # cutoff以下なら全部買う
        cutoff = (ok + ng) // 2
        buy = 0
        total = 0
        buy_cutoff = 0
        total_cutoff = 0

        for a, d in AD:
            bl, sl, b, s = calc_buy(a, d, cutoff)
            buy += bl
            total += sl
            buy_cutoff += b
            total_cutoff += s

        if buy + buy_cutoff >= K:
            ok = cutoff
            if buy < K:
                ans = min(ans, total + (K - buy) * cutoff)
            else:
                ans = min(ans, total)
        else:
            ng = cutoff

    print(ans)


if __name__ == "__main__":
    main()
